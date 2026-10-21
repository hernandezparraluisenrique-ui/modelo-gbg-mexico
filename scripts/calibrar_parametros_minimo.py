
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

from src.modelo.parametros import PARAMETROS
from src.simulacion.simulador import ejecutar_simulacion


# ------------------------------------------------------------
# RUTAS Y CONFIGURACIÓN
# ------------------------------------------------------------

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "serie_mensual_analisis.csv"
SALIDA = RAIZ / "calibracion_minima.csv"

ESTADO_INICIAL = np.array(
    [1000, 500, 200, 1000, 1000, 0, 0],
    dtype=float,
)

DIAS_POR_MES = 365.25 / 12
MESES_PRUEBA = 4


# ------------------------------------------------------------
# CARGA Y PREPARACIÓN DE DATOS
# ------------------------------------------------------------

def cargar_datos():
    if not ENTRADA.exists():
        raise FileNotFoundError(f"No existe el archivo: {ENTRADA}")

    df = pd.read_csv(ENTRADA)

    requeridas = {"periodo", "bovinos", "porcinos"}
    faltantes = requeridas - set(df.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas: {sorted(faltantes)}")

    df["periodo"] = pd.to_datetime(
        df["periodo"].astype(str),
        format="%Y-%m",
        errors="coerce",
    )

    for col in ["bovinos", "porcinos"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Los meses bovinos incompletos no se usan para calibrar.
    if "bovinos_completo" in df.columns:
        completo_bovino = (
            df["bovinos_completo"]
            .astype(str)
            .str.strip()
            .str.lower()
            .eq("si")
        )
    else:
        completo_bovino = df["bovinos"].notna()

    df = df[
        df["periodo"].notna()
        & completo_bovino
        & df["bovinos"].notna()
        & df["porcinos"].notna()
    ].copy()

    df = df.sort_values("periodo").reset_index(drop=True)

    if len(df) < MESES_PRUEBA + 5:
        raise ValueError("No hay suficientes meses completos para calibrar y probar.")

    df["casos"] = df["bovinos"] + df["porcinos"]

    # Tiempo real desde el primer mes del archivo original.
    # No se comprimen los huecos cuando hay meses excluidos.
    df_original = pd.read_csv(ENTRADA)
    fechas_originales = pd.to_datetime(
        df_original["periodo"].astype(str),
        format="%Y-%m",
        errors="coerce",
    ).dropna()

    origen = fechas_originales.min()
    df["meses_desde_inicio"] = (
        (df["periodo"].dt.year - origen.year) * 12
        + df["periodo"].dt.month
        - origen.month
    ).astype(float)

    return df


# ------------------------------------------------------------
# SIMULACIÓN
# ------------------------------------------------------------

def simular_hembras(parametros, tiempos_meses):
    """
    Simula hembras silvestres y las interpola en los meses reales.
    Los tiempos se expresan como meses desde el inicio de la serie.
    """
    tiempos_meses = np.asarray(tiempos_meses, dtype=float)

    if len(tiempos_meses) == 0:
        return np.array([], dtype=float)

    p = dict(PARAMETROS)
    p["b"] = float(parametros[0])
    p["mu_f"] = float(parametros[1])
    p["mu_p"] = float(parametros[2])

    dias_finales = int(np.ceil(max(tiempos_meses) * DIAS_POR_MES))
    dias = np.arange(0, max(dias_finales, 1) + 1, dtype=float)

    resultado = ejecutar_simulacion(
        parametros=p,
        estado_inicial=ESTADO_INICIAL.copy(),
        tiempo=dias,
        modelo="etapas",
    )

    if not resultado.success:
        raise RuntimeError("La simulación no terminó correctamente.")

    hembras = np.interp(
        tiempos_meses * DIAS_POR_MES,
        dias,
        resultado.y[4],
    )

    return np.maximum(hembras, 0.0)


# ------------------------------------------------------------
# AJUSTE
# ------------------------------------------------------------

def ajustar_modelo(df):
    # Separación cronológica: los últimos meses completos se reservan.
    n_prueba = MESES_PRUEBA
    entrenamiento = df.iloc[:-n_prueba].copy()
    prueba = df.iloc[-n_prueba:].copy()

    casos_entrenamiento = entrenamiento["casos"].to_numpy(float)
    tiempos_entrenamiento = entrenamiento["meses_desde_inicio"].to_numpy(float)
    tiempos_prueba = prueba["meses_desde_inicio"].to_numpy(float)

    # x = [b, mu_f, mu_p, escala]
    # La escala relaciona la salida simulada con casos reportados;
    # no es un parámetro biológico.
    def predecir(x, tiempos):
        hembras = simular_hembras(x[:3], tiempos)
        return np.exp(x[3]) * hembras

    def residuos(x):
        pred = predecir(x, tiempos_entrenamiento)
        if not np.isfinite(pred).all():
            return np.full(len(casos_entrenamiento), 1e6)

        return np.log1p(pred) - np.log1p(casos_entrenamiento)

    x0 = [
        float(PARAMETROS["b"]),
        float(PARAMETROS["mu_f"]),
        float(PARAMETROS["mu_p"]),
        np.log(1e-3),
    ]

    limites_inferiores = [0.001, 0.01, 0.005, -20.0]
    limites_superiores = [0.3, 0.3, 0.2, 5.0]

    ajuste = least_squares(
        residuos,
        x0=x0,
        bounds=(limites_inferiores, limites_superiores),
        loss="soft_l1",
        max_nfev=100,
    )

    pred_entrenamiento = predecir(ajuste.x, tiempos_entrenamiento)
    pred_prueba = predecir(ajuste.x, tiempos_prueba)

    rmse_entrenamiento = np.sqrt(
        np.mean(
            (
                np.log1p(pred_entrenamiento)
                - np.log1p(casos_entrenamiento)
            ) ** 2
        )
    )

    casos_prueba = prueba["casos"].to_numpy(float)
    rmse_prueba = np.sqrt(
        np.mean(
            (np.log1p(pred_prueba) - np.log1p(casos_prueba)) ** 2
        )
    )

    entrenamiento["grupo"] = "calibracion"
    entrenamiento["casos_predichos"] = pred_entrenamiento

    prueba["grupo"] = "prueba"
    prueba["casos_predichos"] = pred_prueba

    salida = pd.concat([entrenamiento, prueba], ignore_index=True)
    salida["error_absoluto"] = abs(
        salida["casos"] - salida["casos_predichos"]
    )

    return salida, ajuste, rmse_entrenamiento, rmse_prueba


# ------------------------------------------------------------
# EJECUCIÓN
# ------------------------------------------------------------

def main():
    df = cargar_datos()

    salida, ajuste, rmse_entrenamiento, rmse_prueba = ajustar_modelo(df)

    salida.to_csv(SALIDA, index=False, encoding="utf-8-sig")

    print("\nCALIBRACIÓN DEL MODELO GBG")
    print("=" * 45)
    print(f"Meses completos disponibles: {len(df)}")
    print(f"Filas de calibración: {(salida['grupo'] == 'calibracion').sum()}")
    print(f"Filas de prueba: {(salida['grupo'] == 'prueba').sum()}")
    print(f"Optimización finalizada: {ajuste.success}")
    print("\nParámetros ajustados:")
    print(f"b     = {ajuste.x[0]:.6g}")
    print(f"mu_f  = {ajuste.x[1]:.6g}")
    print(f"mu_p  = {ajuste.x[2]:.6g}")
    print(f"escala empírica = {np.exp(ajuste.x[3]):.6g}")
    print(f"\nRMSE log calibración: {rmse_entrenamiento:.4f}")
    print(f"RMSE log prueba:      {rmse_prueba:.4f}")

    print("\nComparación de meses reservados:")
    print(
        salida.loc[
            salida["grupo"] == "prueba",
            ["periodo", "casos", "casos_predichos", "error_absoluto"],
        ].to_string(index=False)
    )

    print(f"\nArchivo generado: {SALIDA}")
    print(
        "\nAdvertencia: la escala es empírica. Un ajuste numérico no "
        "demuestra validez biológica ni permite estimar liberaciones reales."
    )


if __name__ == "__main__":
    main()
