from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "serie_mensual_analisis.csv"
SALIDA = RAIZ / "validacion_temporal_referencia.csv"

HOSPEDADORES = ("bovinos", "porcinos")
MESES_PRUEBA = 4


def ajustar_curva(t, casos):
    """Ajusta una curva descriptiva usando únicamente la calibración."""
    t = np.asarray(t, dtype=float)
    casos = np.asarray(casos, dtype=float)
    objetivo = np.log1p(casos)

    centro_inicial = float(t[np.argmax(casos)])
    amplitud_inicial = max(float(objetivo.max()), 0.1)

    def predecir_log(p, x):
        a, b, amplitud, centro, log_ancho = p
        ancho = np.exp(log_ancho)
        return (
            a + b * x
            + amplitud * np.exp(
                -0.5 * ((x - centro) / ancho) ** 2
            )
        )

    def residuos(p):
        return predecir_log(p, t) - objetivo

    inicio = [
        max(float(objetivo.min()), 0.0),
        0.0,
        amplitud_inicial,
        centro_inicial,
        np.log(max(len(t) / 4, 1.0)),
    ]

    inferior = [
        -10.0, -2.0, 0.0,
        float(t.min()) - len(t), np.log(0.5)
    ]

    superior = [
        10.0, 2.0, 15.0,
        float(t.max()) + len(t),
        np.log(max(len(t) * 2, 1.0))
    ]

    ajuste = least_squares(
        residuos,
        x0=inicio,
        bounds=(inferior, superior),
        loss="soft_l1",
        max_nfev=20000,
    )

    pred = np.maximum(
        0.0,
        np.expm1(predecir_log(ajuste.x, t))
    )

    return pred, bool(ajuste.success)


def main():
    if not ENTRADA.exists():
        raise FileNotFoundError(f"No existe: {ENTRADA}")

    df = pd.read_csv(ENTRADA)

    requeridas = {
        "periodo",
        "bovinos",
        "porcinos",
        "bovinos_completo",
        "porcinos_completo",
    }

    faltantes = requeridas - set(df.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas: {sorted(faltantes)}")

    df["periodo"] = pd.to_datetime(
        df["periodo"].astype(str),
        format="%Y-%m",
        errors="coerce",
    )
    df = (
        df.dropna(subset=["periodo"])
        .sort_values("periodo")
        .reset_index(drop=True)
    )

    resultados = []

    for hospedador in HOSPEDADORES:
        casos = pd.to_numeric(df[hospedador], errors="coerce")

        completos = (
            df[f"{hospedador}_completo"]
            .astype(str).str.strip().str.lower().eq("si")
        )

        validos = casos.notna() & completos
        serie = df.loc[validos].copy()
        serie["casos"] = casos.loc[validos].to_numpy()

        if len(serie) < 10:
            print(f"Se omite {hospedador}: hay menos de 10 meses.")
            continue

        # Se reservan los últimos cuatro meses completos.
        corte = len(serie) - MESES_PRUEBA
        entrenamiento = serie.iloc[:corte].copy()
        prueba = serie.iloc[corte:].copy()

        # Mantener el tiempo real transcurrido entre meses.
        origen = serie["periodo"].min()
        t_entrenamiento = (
            (entrenamiento["periodo"].dt.year - origen.year) * 12
            + entrenamiento["periodo"].dt.month - origen.month
        ).to_numpy(dtype=float)

        t_prueba = (
            (prueba["periodo"].dt.year - origen.year) * 12
            + prueba["periodo"].dt.month - origen.month
        ).to_numpy(dtype=float)

        pred_entrenamiento, exitoso = ajustar_curva(
            t_entrenamiento,
            entrenamiento["casos"].to_numpy(dtype=float),
        )

        # Para predecir meses futuros se ajusta la misma familia
        # de curvas y se evalúa en las posiciones reservadas.
        # El centro y el ancho se estiman solo con entrenamiento.
        y = np.log1p(entrenamiento["casos"].to_numpy(dtype=float))

        def predecir_log(p, x):
            a, b, amplitud, centro, log_ancho = p
            ancho = np.exp(log_ancho)
            return a + b * x + amplitud * np.exp(
                -0.5 * ((x - centro) / ancho) ** 2
            )

        centro_inicial = float(t_entrenamiento[np.argmax(y)])
        inicio = [
            max(float(y.min()), 0.0),
            0.0,
            max(float(y.max()), 0.1),
            centro_inicial,
            np.log(max(len(y) / 4, 1.0)),
        ]

        def residuos(p):
            return predecir_log(p, t_entrenamiento) - y

        ajuste = least_squares(
            residuos,
            x0=inicio,
            bounds=(
                [-10, -2, 0, t_entrenamiento.min() - len(y), np.log(0.5)],
                [10, 2, 15, t_entrenamiento.max() + len(y),
                 np.log(max(len(y) * 2, 1.0))],
            ),
            loss="soft_l1",
            max_nfev=20000,
        )

        pred_prueba = np.maximum(
            0.0,
            np.expm1(predecir_log(ajuste.x, t_prueba)),
        )

        observados = prueba["casos"].to_numpy(dtype=float)
        errores = observados - pred_prueba

        rmse = float(np.sqrt(np.mean(errores ** 2)))
        mae = float(np.mean(np.abs(errores)))
        rmse_log = float(np.sqrt(np.mean(
            (np.log1p(observados) - np.log1p(pred_prueba)) ** 2
        )))

        print(f"\n--- {hospedador.upper()} ---")
        print(f"Meses de calibración: {len(entrenamiento)}")
        print(f"Meses reservados: {len(prueba)}")
        print(f"MAE de prueba: {mae:.3f}")
        print(f"RMSE de prueba: {rmse:.3f}")
        print(f"RMSE logarítmico de prueba: {rmse_log:.4f}")
        print(f"Optimización exitosa: {ajuste.success}")

        for (_, fila), pred, error in zip(
            prueba.iterrows(), pred_prueba, errores
        ):
            resultados.append({
                "hospedador": hospedador,
                "periodo": fila["periodo"].strftime("%Y-%m"),
                "grupo": "prueba_temporal",
                "casos_observados": float(fila["casos"]),
                "casos_predichos": float(pred),
                "error": float(error),
                "error_absoluto": float(abs(error)),
                "mae_prueba": mae,
                "rmse_prueba": rmse,
                "rmse_log_prueba": rmse_log,
                "ajuste_exitoso": bool(ajuste.success),
            })

    if not resultados:
        raise RuntimeError("No se pudo validar ninguna serie.")

    salida = pd.DataFrame(resultados)
    salida.to_csv(SALIDA, index=False, encoding="utf-8-sig")

    print(f"\nArchivo generado: {SALIDA}")
    print(
        "\nImportante: la prueba evalúa la predicción de casos reportados; "
        "no valida el modelo biológico de poblaciones de moscas."
    )


if __name__ == "__main__":
    main()