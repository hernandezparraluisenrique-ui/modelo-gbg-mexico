
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "serie_mensual_analisis.csv"
SALIDA = RAIZ / "calibracion_casos.csv"


def ajustar_serie(valores):
    y = pd.to_numeric(valores, errors="coerce")
    y = y.dropna().to_numpy(dtype=float)

    if len(y) < 5:
        return None

    t = np.arange(len(y), dtype=float)

    # Modelo descriptivo: log(casos + 1) = a + b*t.
    # No representa directamente la dinámica de las moscas.
    objetivo = np.log1p(y)

    def residuos(p):
        a, b = p
        return a + b * t - objetivo

    ajuste = least_squares(
        residuos,
        x0=[float(np.mean(objetivo)), 0.0],
        loss="soft_l1",
    )

    a, b = ajuste.x

    return {
        "meses_validos": len(y),
        "casos_totales": float(y.sum()),
        "pendiente_log_mensual": float(b),
        "cambio_porcentual_mensual_aprox": float(
            100 * np.expm1(b)
        ),
        "ajuste_exitoso": bool(ajuste.success),
    }


def main():
    df = pd.read_csv(ENTRADA)

    resultados = []

    for hospedador in ("bovinos", "porcinos"):
        resultado = ajustar_serie(df[hospedador])

        if resultado is not None:
            resultado["hospedador"] = hospedador
            resultados.append(resultado)

    salida = pd.DataFrame(resultados)
    salida.to_csv(SALIDA, index=False, encoding="utf-8-sig")

    print(salida.to_string(index=False))
    print(f"\nArchivo generado: {SALIDA}")
    print(
        "\nInterpretación: tendencia de casos reportados; "
        "no estima moscas silvestres ni causalidad."
    )


if __name__ == "__main__":
    main()
