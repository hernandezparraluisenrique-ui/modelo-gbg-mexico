
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

from src.modelo.parametros import PARAMETROS
from src.simulacion.simulador import ejecutar_simulacion


# ============================================================
# RUTAS
# ============================================================

RAIZ = Path(__file__).resolve().parent.parent

ARCHIVO_DATOS = RAIZ / "serie_mensual_analisis.csv"
ARCHIVO_RESULTADOS = RAIZ / "calibracion_modelo_etapas.csv"

# Estado del modelo:
# H = huevos
# L = larvas
# P = pupas silvestres
# Mw = machos silvestres
# Fw = hembras silvestres
# Ps = pupas en planta
# Ms = machos estériles
ESTADO_INICIAL = np.array(
    [1000, 500, 200, 1000, 1000, 0, 0],
    dtype=float,
)

DIAS_POR_MES = 365.25 / 12
DIAS_SIMULACION = 730


# ============================================================
# SIMULACIÓN
# ============================================================

def simular_hembras(parametros, numero_meses):
    """
    Ejecuta el modelo por etapas y obtiene las hembras silvestres
    simuladas al inicio de cada mes.

    Los parámetros biológicos son los definidos en PARAMETROS.
    """

    dias_necesarios = int(np.ceil((numero_meses - 1) * DIAS_POR_MES))

    if dias_necesarios > DIAS_SIMULACION:
        raise ValueError(
            "El periodo solicitado supera la duración de la simulación."
        )

    tiempos_dias = np.arange(
        0,
        DIAS_SIMULACION + 1,
        1,
        dtype=float,
    )

    resultado = ejecutar_simulacion(
        parametros=parametros,
        estado_inicial=ESTADO_INICIAL.copy(),
        tiempo=tiempos_dias,
        modelo="etapas",
    )

    if not resultado.success:
        raise RuntimeError("La simulación no terminó correctamente.")

    dias_muestreo = np.arange(
        numero_meses,
        dtype=float,
    ) * DIAS_POR_MES

    hembras = np.interp(
        dias_muestreo,
        tiempos_dias,
        resultado.y[4],
    )

    return hembras


# ============================================================
# AJUSTE DE CASOS OBSERVADOS
# ============================================================

def ajustar_serie(casos, hembras):
    """
    Ajusta una escala empírica entre hembras simuladas y casos:

        casos ajustados = escala * hembras simuladas

    Se ajusta en escala logarítmica para reducir la influencia
    excesiva de los meses con muchos casos.

    La escala no representa una tasa biológica conocida.
    """

    casos = np.asarray(casos, dtype=float)
    hembras = np.asarray(hembras, dtype=float)

    validos = (
        np.isfinite(casos)
        & np.isfinite(hembras)
        & (casos >= 0)
        & (hembras >= 0)
    )

    casos = casos[validos]
    hembras = hembras[validos]

    if len(casos) < 5:
        raise ValueError(
            "Se necesitan al menos cinco meses válidos para ajustar."
        )

    objetivo = np.log1p(casos)

    def residuos(parametros_ajuste):
        escala = np.exp(parametros_ajuste[0])
        prediccion = escala * hembras

        return np.log1p(prediccion) - objetivo

    escala_inicial = (
        max(float(casos.mean()), 1e-6)
        / max(float(hembras.mean()), 1e-6)
    )

    ajuste = least_squares(
        residuos,
        x0=[np.log(escala_inicial)],
        loss="soft_l1",
    )

    escala = float(np.exp(ajuste.x[0]))
    prediccion = escala * hembras

    error_log = float(
        np.sqrt(
            np.mean(
                (np.log1p(prediccion) - objetivo) ** 2
            )
        )
    )

    return {
        "escala": escala,
        "predicciones": prediccion,
        "error_log_rmse": error_log,
        "ajuste_exitoso": bool(ajuste.success),
        "meses_ajustados": len(casos),
    }


# ============================================================
# PROCESAMIENTO DE DATOS
# ============================================================

def main():
    if not ARCHIVO_DATOS.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de datos: {ARCHIVO_DATOS}"
        )

    datos = pd.read_csv(ARCHIVO_DATOS)

    # Comprobar las columnas necesarias.
    if "periodo" not in datos.columns:
        raise ValueError(
            "Falta la columna 'periodo'. "
            f"Columnas encontradas: {datos.columns.tolist()}"
        )

    datos["periodo"] = pd.to_datetime(
        datos["periodo"].astype(str),
        format="%Y-%m",
        errors="coerce",
    )

    datos = (
        datos.dropna(subset=["periodo"])
        .sort_values("periodo")
        .reset_index(drop=True)
    )

    hospedadores = ("bovinos", "porcinos")

    for hospedador in hospedadores:
        if hospedador not in datos.columns:
            raise ValueError(
                f"Falta la columna '{hospedador}' en el CSV."
            )

    # Comprobar la disponibilidad de los datos completos.
    # Se simula toda la serie en orden cronológico.
    hembras = simular_hembras(
        parametros=PARAMETROS,
        numero_meses=len(datos),
    )

    # Esta simulación usa la producción ficticia definida en
    # PARAMETROS. No debe interpretarse como un escenario real.
    resultados = []

    for hospedador in hospedadores:
        columna_completo = f"{hospedador}_completo"

        casos = pd.to_numeric(
            datos[hospedador],
            errors="coerce",
        )

        if columna_completo in datos.columns:
            completos = (
                datos[columna_completo]
                .astype(str)
                .str.strip()
                .str.lower()
                .eq("si")
            )
        else:
            completos = casos.notna()

        validos = casos.notna() & completos

        casos_validos = casos.loc[validos].to_numpy(dtype=float)
        hembras_validas = hembras[validos.to_numpy()]

        if len(casos_validos) < 5:
            print(
                f"\nSe omite {hospedador}: "
                "menos de cinco meses completos."
            )
            continue

        ajuste = ajustar_serie(
            casos_validos,
            hembras_validas,
        )

        fechas = (
            datos.loc[validos, "periodo"]
            .dt.strftime("%Y-%m")
            .to_numpy()
        )

        print(f"\nHospedador: {hospedador}")
        print(f"Meses completos utilizados: {ajuste['meses_ajustados']}")
        print(f"Escala empírica ajustada: {ajuste['escala']:.8g}")
        print(f"RMSE de log(1 + casos): {ajuste['error_log_rmse']:.4f}")
        print(f"Ajuste exitoso: {ajuste['ajuste_exitoso']}")

        for fecha, observado, hembras_mes, estimado in zip(
            fechas,
            casos_validos,
            hembras_validas,
            ajuste["predicciones"],
        ):
            resultados.append(
                {
                    "periodo": fecha,
                    "hospedador": hospedador,
                    "casos_observados": observado,
                    "hembras_simuladas": hembras_mes,
                    "casos_ajustados": estimado,
                    "escala_empirica": ajuste["escala"],
                    "error_log_rmse": ajuste["error_log_rmse"],
                    "ajuste_exitoso": ajuste["ajuste_exitoso"],
                }
            )

    if not resultados:
        raise RuntimeError(
            "No se pudo ajustar ninguna serie. "
            "Revisa los datos y las columnas de completitud."
        )

    salida = pd.DataFrame(resultados)

    salida.to_csv(
        ARCHIVO_RESULTADOS,
        index=False,
        encoding="utf-8-sig",
    )

    print("\n" + "=" * 55)
    print("CALIBRACIÓN DESCRIPTIVA TERMINADA")
    print("=" * 55)
    print(f"Archivo generado: {ARCHIVO_RESULTADOS}")
    print(f"Filas generadas: {len(salida)}")
    print(
        "\nAdvertencia: el ajuste relaciona casos observados con "
        "una simulación basada en parámetros hipotéticos."
    )
    print(
        "No estima por sí solo la población real de moscas, "
        "la cantidad necesaria de moscas estériles ni el tiempo "
        "nacional de erradicación."
    )


if __name__ == "__main__":
    main()
