
from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

from src.modelo.modelo_etapas import modelo_gbg_etapas
from src.modelo.parametros import PARAMETROS


RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO_SALIDA = RAIZ / "sensibilidad_parametros.csv"

ESTADO_INICIAL = np.array(
    [1000, 500, 200, 1000, 1000, 0, 0],
    dtype=float,
)
DIAS = 180
DIAS_EVALUACION = [30, 90, 180]

# Factores de prueba relativos al valor base.
FACTORES = [0.5, 0.75, 1.0, 1.25, 1.5]

# Parámetros a estudiar individualmente.
PARAMETROS_ESTUDIAR = [
    "b",
    "k_h",
    "k_l",
    "k_p",
    "mu_h",
    "mu_l",
    "mu_p",
    "mu_m",
    "mu_f",
    "c",
]


def simular(parametros):
    tiempos = np.arange(DIAS + 1, dtype=float)

    resultado = solve_ivp(
        lambda t, y: modelo_gbg_etapas(t, y, parametros),
        (0, DIAS),
        ESTADO_INICIAL.copy(),
        t_eval=tiempos,
        rtol=1e-7,
        atol=1e-9,
    )

    if not resultado.success:
        raise RuntimeError(resultado.message)

    if not np.all(np.isfinite(resultado.y)):
        raise RuntimeError("La simulación produjo valores no finitos.")

    hembras = np.maximum(resultado.y[4], 0)

    return {
        dia: float(hembras[dia])
        for dia in DIAS_EVALUACION
    }


def main():
    base = deepcopy(PARAMETROS)

    # Aísla la población silvestre: no hay producción ni
    # liberación de machos estériles en este experimento.
    base["produccion_pupas"] = lambda t: 0.0

    resultado_base = simular(base)
    filas = []

    print("Hembras silvestres en el escenario base")
    for dia, valor in resultado_base.items():
        print(f"Día {dia}: {valor:.4f}")

    for nombre in PARAMETROS_ESTUDIAR:
        valor_base = float(base[nombre])

        for factor in FACTORES:
            if factor == 1.0:
                resultado = resultado_base
            else:
                parametros = deepcopy(base)
                parametros[nombre] = valor_base * factor
                resultado = simular(parametros)

            fila = {
                "parametro": nombre,
                "valor_base": valor_base,
                "factor_aplicado": factor,
                "valor_probado": valor_base * factor,
            }

            for dia in DIAS_EVALUACION:
                fila[f"hembras_dia_{dia}"] = resultado[dia]

                valor_referencia = resultado_base[dia]
                if valor_referencia > 1e-12:
                    cambio_pct = (
                        100
                        * (resultado[dia] - valor_referencia)
                        / valor_referencia
                    )
                else:
                    cambio_pct = np.nan

                fila[f"cambio_pct_dia_{dia}"] = cambio_pct

            filas.append(fila)

    tabla = pd.DataFrame(filas)
    tabla.to_csv(
        ARCHIVO_SALIDA,
        index=False,
        encoding="utf-8-sig",
    )

    print("\nMayor efecto relativo al día 180:")
    resumen = tabla.loc[
        tabla["factor_aplicado"] != 1.0
    ].copy()

    resumen["magnitud_cambio"] = resumen[
        "cambio_pct_dia_180"
    ].abs()

    print(
        resumen.sort_values(
            "magnitud_cambio",
            ascending=False,
        )[
            [
                "parametro",
                "factor_aplicado",
                "hembras_dia_180",
                "cambio_pct_dia_180",
            ]
        ].head(10).round(3).to_string(index=False)
    )

    print(f"\nArchivo generado: {ARCHIVO_SALIDA}")
    print(
        "\nAdvertencia: este análisis mide sensibilidad del modelo "
        "con parámetros hipotéticos; no demuestra efectos reales "
        "ni calcula liberaciones necesarias."
    )


if __name__ == "__main__":
    main()
