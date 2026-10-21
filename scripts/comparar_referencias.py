
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "serie_mensual_analisis.csv"
VALIDACION = RAIZ / "validacion_temporal_referencia.csv"

MESES_PRUEBA = 4


def calcular_metricas(observados, predichos):
    errores = observados - predichos

    return {
        "MAE": np.mean(np.abs(errores)),
        "RMSE": np.sqrt(np.mean(errores ** 2)),
        "RMSE_log": np.sqrt(
            np.mean(
                (
                    np.log1p(observados)
                    - np.log1p(np.maximum(predichos, 0))
                ) ** 2
            )
        ),
    }


def main():
    df = pd.read_csv(ENTRADA)
    validacion = pd.read_csv(VALIDACION)

    df["periodo"] = pd.to_datetime(
        df["periodo"],
        format="%Y-%m",
        errors="coerce",
    )

    df = (
        df.dropna(subset=["periodo"])
        .sort_values("periodo")
        .reset_index(drop=True)
    )

    for hospedador in ("bovinos", "porcinos"):
        casos = pd.to_numeric(
            df[hospedador],
            errors="coerce",
        )

        completos = (
            df[f"{hospedador}_completo"]
            .astype(str)
            .str.strip()
            .str.lower()
            .eq("si")
        )

        serie = df.loc[casos.notna() & completos].copy()
        serie["casos"] = casos.loc[
            casos.notna() & completos
        ].to_numpy()

        if len(serie) <= MESES_PRUEBA:
            print(f"No hay datos suficientes: {hospedador}")
            continue

        corte = len(serie) - MESES_PRUEBA
        entrenamiento = serie.iloc[:corte]
        prueba = serie.iloc[corte:]

        observado = prueba["casos"].to_numpy(dtype=float)

        predicciones = {
            "Último valor": np.repeat(
                float(entrenamiento["casos"].iloc[-1]),
                len(prueba),
            ),
            "Promedio histórico": np.repeat(
                float(entrenamiento["casos"].mean()),
                len(prueba),
            ),
        }

        modelo = validacion[
            (validacion["hospedador"] == hospedador)
            & (validacion["grupo"] == "prueba_temporal")
        ].copy()

        modelo["periodo"] = pd.to_datetime(
            modelo["periodo"],
            format="%Y-%m",
        )

        periodos_prueba = prueba["periodo"].dt.strftime(
            "%Y-%m"
        ).tolist()

        modelo = (
            modelo.set_index("periodo")
            .reindex(prueba["periodo"])
        )

        if modelo["casos_predichos"].isna().any():
            print(
                f"\nNo coinciden los meses de prueba "
                f"del modelo para {hospedador}."
            )
            continue

        predicciones["Curva actual"] = modelo[
            "casos_predichos"
        ].to_numpy(dtype=float)

        print(f"\n--- {hospedador.upper()} ---")
        print("Meses de prueba:", ", ".join(periodos_prueba))

        for nombre, predichos in predicciones.items():
            metricas = calcular_metricas(observado, predichos)

            print(f"\n{nombre}")
            for metrica, valor in metricas.items():
                print(f"  {metrica}: {valor:.4f}")


if __name__ == "__main__":
    main()
