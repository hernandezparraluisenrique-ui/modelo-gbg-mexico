
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import least_squares


RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO_ENTRADA = RAIZ / "serie_mensual_analisis.csv"
ARCHIVO_SALIDA = RAIZ / "curva_referencia_casos.csv"

HOSPEDADORES = ("bovinos", "porcinos")


def ajustar_curva(t, casos):
    """
    Ajusta una curva de referencia con un pico gaussiano y una
    tendencia exponencial de fondo.

    Es una descripción empírica de los casos, no un modelo
    biológico ni una predicción de la población de moscas.
    """
    t = np.asarray(t, dtype=float)
    casos = np.asarray(casos, dtype=float)

    if len(casos) < 5:
        raise ValueError(
            "Se requieren al menos cinco meses completos."
        )

    # La curva tiene:
    # fondo(t) = exp(a + b*t)
    # pico(t) = amplitud * exp(-0.5*((t-centro)/ancho)**2)
    #
    # Se ajusta log(1 + casos) para estabilizar la influencia
    # de los picos grandes.
    log_casos = np.log1p(casos)

    indice_pico = int(np.argmax(casos))
    centro_inicial = float(t[indice_pico])
    amplitud_inicial = max(float(log_casos.max()), 0.1)

    def predecir_log(parametros, x):
        a, b, amplitud, centro, log_ancho = parametros
        ancho = np.exp(log_ancho)

        fondo = a + b * x
        pico = amplitud * np.exp(
            -0.5 * ((x - centro) / ancho) ** 2
        )

        return fondo + pico

    def residuos(parametros):
        return predecir_log(parametros, t) - log_casos

    inicio = [
        max(float(log_casos.min()), 0.0),
        0.0,
        amplitud_inicial,
        centro_inicial,
        np.log(max(len(t) / 4, 1.0)),
    ]

    inferior = [
        -10.0,
        -2.0,
        0.0,
        float(t.min()) - len(t),
        np.log(0.5),
    ]

    superior = [
        10.0,
        2.0,
        15.0,
        float(t.max()) + len(t),
        np.log(max(len(t) * 2, 1.0)),
    ]

    ajuste = least_squares(
        residuos,
        x0=inicio,
        bounds=(inferior, superior),
        loss="soft_l1",
        max_nfev=20000,
    )

    prediccion = np.maximum(
        0.0,
        np.expm1(predecir_log(ajuste.x, t)),
    )

    rmse = float(
        np.sqrt(np.mean((casos - prediccion) ** 2))
    )

    rmse_log = float(
        np.sqrt(
            np.mean(
                (np.log1p(casos) - np.log1p(prediccion)) ** 2
            )
        )
    )

    return prediccion, rmse, rmse_log, bool(ajuste.success)


def main():
    if not ARCHIVO_ENTRADA.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {ARCHIVO_ENTRADA}"
        )

    datos = pd.read_csv(ARCHIVO_ENTRADA)

    requeridas = {
        "periodo",
        "bovinos",
        "porcinos",
        "bovinos_completo",
        "porcinos_completo",
    }

    faltantes = requeridas - set(datos.columns)
    if faltantes:
        raise ValueError(
            f"Faltan columnas en el CSV: {sorted(faltantes)}"
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

    resultados = []

    for hospedador in HOSPEDADORES:
        columna_completo = f"{hospedador}_completo"

        casos = pd.to_numeric(
            datos[hospedador],
            errors="coerce",
        )

        completos = (
            datos[columna_completo]
            .astype(str)
            .str.strip()
            .str.lower()
            .eq("si")
        )

        validos = casos.notna() & completos
        serie = datos.loc[validos].copy()
        valores = casos.loc[validos].to_numpy(dtype=float)

        if len(valores) < 5:
            print(
                f"Se omite {hospedador}: "
                "menos de cinco meses completos."
            )
            continue

        # La posición temporal conserva la distancia real entre
        # meses, incluso si se excluyen meses incompletos.
        posiciones = (
            serie["periodo"].dt.year.to_numpy() * 12
            + serie["periodo"].dt.month.to_numpy()
        )
        t = posiciones - posiciones.min()

        prediccion, rmse, rmse_log, exitoso = ajustar_curva(
            t,
            valores,
        )

        print(f"\n--- {hospedador.upper()} ---")
        print(f"Meses completos: {len(valores)}")
        print(f"Casos observados acumulados: {valores.sum():.0f}")
        print(f"RMSE en casos: {rmse:.2f}")
        print(f"RMSE logarítmico: {rmse_log:.4f}")
        print(f"Ajuste exitoso: {exitoso}")

        for fecha, observado, estimado in zip(
            serie["periodo"],
            valores,
            prediccion,
        ):
            resultados.append(
                {
                    "periodo": fecha.strftime("%Y-%m"),
                    "hospedador": hospedador,
                    "casos_observados": observado,
                    "casos_ajustados": estimado,
                    "residuo": observado - estimado,
                    "rmse_casos": rmse,
                    "rmse_log": rmse_log,
                    "ajuste_exitoso": exitoso,
                }
            )

        plt.figure(figsize=(10, 5))
        plt.plot(
            serie["periodo"],
            valores,
            marker="o",
            label="Casos observados",
        )
        plt.plot(
            serie["periodo"],
            prediccion,
            marker="s",
            linestyle="--",
            label="Curva de referencia",
        )
        plt.title(f"Curva de referencia: {hospedador}")
        plt.xlabel("Mes")
        plt.ylabel("Casos reportados")
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()

        archivo_grafica = (
            RAIZ / f"curva_referencia_{hospedador}.png"
        )
        plt.savefig(archivo_grafica, dpi=150)
        plt.close()

        print(f"Gráfica: {archivo_grafica}")

    if not resultados:
        raise RuntimeError("No se pudo ajustar ninguna serie.")

    salida = pd.DataFrame(resultados)
    salida.to_csv(
        ARCHIVO_SALIDA,
        index=False,
        encoding="utf-8-sig",
    )

    print("\nProceso terminado.")
    print(f"CSV generado: {ARCHIVO_SALIDA}")
    print(
        "\nNota: la curva resume los casos observados. "
        "No estima moscas silvestres ni demuestra el efecto "
        "de las liberaciones estériles."
    )


if __name__ == "__main__":
    main()


