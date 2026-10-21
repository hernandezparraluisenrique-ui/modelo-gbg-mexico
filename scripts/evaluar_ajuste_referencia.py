
from pathlib import Path

import numpy as np
import pandas as pd


RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO = RAIZ / "curva_referencia_casos.csv"
SALIDA_DETALLE = RAIZ / "evaluacion_ajuste_referencia.csv"
SALIDA_RESUMEN = RAIZ / "resumen_evaluacion_referencia.csv"


def calcular_metricas(observados, ajustados):
    observados = np.asarray(observados, dtype=float)
    ajustados = np.asarray(ajustados, dtype=float)

    error = ajustados - observados
    mae = float(np.mean(np.abs(error)))
    rmse = float(np.sqrt(np.mean(error**2)))
    rmse_log = float(
        np.sqrt(
            np.mean(
                (np.log1p(ajustados) - np.log1p(observados)) ** 2
            )
        )
    )

    total_observado = float(observados.sum())
    total_ajustado = float(ajustados.sum())

    if np.sum((observados - observados.mean()) ** 2) > 0:
        ss_res = float(np.sum(error**2))
        ss_tot = float(
            np.sum((observados - observados.mean()) ** 2)
        )
        r2 = 1.0 - ss_res / ss_tot
    else:
        r2 = np.nan

    if total_observado > 0:
        error_total_pct = (
            100.0
            * (total_ajustado - total_observado)
            / total_observado
        )
    else:
        error_total_pct = np.nan

    return {
        "n_meses": len(observados),
        "total_observado": total_observado,
        "total_ajustado": total_ajustado,
        "MAE": mae,
        "RMSE": rmse,
        "RMSE_log1p": rmse_log,
        "R2_descriptivo": r2,
        "error_total_porcentual": error_total_pct,
    }


def main():
    if not ARCHIVO.exists():
        raise FileNotFoundError(
            f"No se encontró {ARCHIVO}. "
            "Ejecuta primero scripts.ajustar_curva_referencia."
        )

    datos = pd.read_csv(ARCHIVO)

    requeridas = {
        "periodo",
        "hospedador",
        "casos_observados",
        "casos_ajustados",
    }
    faltantes = requeridas - set(datos.columns)

    if faltantes:
        raise ValueError(
            f"Faltan columnas en el archivo: {sorted(faltantes)}"
        )

    for columna in ("casos_observados", "casos_ajustados"):
        datos[columna] = pd.to_numeric(
            datos[columna],
            errors="coerce",
        )

    datos = datos.dropna(
        subset=["periodo", "hospedador",
                "casos_observados", "casos_ajustados"]
    ).copy()

    datos["error"] = (
        datos["casos_ajustados"] - datos["casos_observados"]
    )
    datos["error_absoluto"] = datos["error"].abs()
    datos["error_log_absoluto"] = np.abs(
        np.log1p(datos["casos_ajustados"].clip(lower=0))
        - np.log1p(datos["casos_observados"].clip(lower=0))
    )

    resumen = []

    for hospedador, grupo in datos.groupby("hospedador"):
        metricas = calcular_metricas(
            grupo["casos_observados"],
            grupo["casos_ajustados"],
        )
        metricas["hospedador"] = hospedador
        resumen.append(metricas)

    resumen_df = pd.DataFrame(resumen)

    # Ordenar columnas para facilitar su lectura.
    columnas = [
        "hospedador",
        "n_meses",
        "total_observado",
        "total_ajustado",
        "MAE",
        "RMSE",
        "RMSE_log1p",
        "R2_descriptivo",
        "error_total_porcentual",
    ]
    resumen_df = resumen_df[columnas]

    datos.to_csv(
        SALIDA_DETALLE,
        index=False,
        encoding="utf-8-sig",
    )
    resumen_df.to_csv(
        SALIDA_RESUMEN,
        index=False,
        encoding="utf-8-sig",
    )

    print("\n=== EVALUACIÓN DE LA CURVA DE REFERENCIA ===")
    print(
        resumen_df.round(4).to_string(index=False)
    )

    print("\n=== MAYORES ERRORES POR HOSPEDADOR ===")
    for hospedador, grupo in datos.groupby("hospedador"):
        peores = grupo.nlargest(5, "error_absoluto")
        print(f"\n{hospedador}:")
        print(
            peores[
                [
                    "periodo",
                    "casos_observados",
                    "casos_ajustados",
                    "error",
                ]
            ].round(2).to_string(index=False)
        )

    print(f"\nDetalle: {SALIDA_DETALLE}")
    print(f"Resumen: {SALIDA_RESUMEN}")
    print(
        "\nInterpretación: estas métricas evalúan una curva "
        "descriptiva de casos; no validan el modelo biológico "
        "ni estiman la población de moscas."
    )


if __name__ == "__main__":
    main()


