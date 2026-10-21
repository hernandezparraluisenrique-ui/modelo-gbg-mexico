
from copy import deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

from src.modelo.modelo_etapas import modelo_gbg_etapas
from src.modelo.parametros import PARAMETROS


BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_SALIDA = BASE_DIR / "escenarios_liberacion.csv"

# Escenarios exploratorios, NO capacidades verificadas de una planta.
CAPACIDADES_PUPAS_DIA = [0, 1_000, 10_000, 100_000]

DIAS = 365

# Estado inicial: H, L, P, Mw, Fw, Ps, Ms.
ESTADO_INICIAL = [1000, 500, 200, 1000, 1000, 0, 0]


def simular(capacidad_pupas_dia):
    parametros = deepcopy(PARAMETROS)

    # Sustituye la producción fija por la capacidad del escenario.
    parametros["produccion_pupas"] = (
        lambda t: float(capacidad_pupas_dia)
    )

    # Estado adicional: acumulado total de machos liberados.
    def sistema(t, estado):
        poblacion = estado[:7]
        derivadas = modelo_gbg_etapas(t, poblacion, parametros)

        machos_en_campo = max(0.0, poblacion[6])
        liberacion_dia = max(
            0.0,
            derivadas[6] + parametros["mu_s"] * machos_en_campo,
        )

        return [*derivadas, liberacion_dia]

    tiempos = np.arange(0, DIAS + 1, dtype=float)

    resultado = solve_ivp(
        sistema,
        (0, DIAS),
        [*ESTADO_INICIAL, 0.0],
        t_eval=tiempos,
        rtol=1e-7,
        atol=1e-9,
    )

    if not resultado.success:
        raise RuntimeError(resultado.message)

    datos = resultado.y
    return {
        "capacidad_pupas_dia": capacidad_pupas_dia,
        "dias_simulados": DIAS,
        "liberados_acumulados": datos[7, -1],
        "machos_esteriles_vivos_dia_final": datos[6, -1],
        "machos_silvestres_dia_final": datos[3, -1],
        "hembras_silvestres_dia_final": datos[4, -1],
        "minimo_poblacion_silvestre": np.min(datos[:5]),
        "integracion_exitosa": resultado.success,
        "tipo_resultado": "exploratorio; parametros biologicos no calibrados",
    }


def main():
    filas = [simular(capacidad) for capacidad in CAPACIDADES_PUPAS_DIA]
    tabla = pd.DataFrame(filas)
    tabla.to_csv(ARCHIVO_SALIDA, index=False, encoding="utf-8-sig")

    print(tabla.to_string(index=False))
    print(f"\nResultados guardados en: {ARCHIVO_SALIDA}")
    print(
        "\nIMPORTANTE: escenarios hipotéticos. No son una "
        "estimación validada para México ni un criterio de erradicación."
    )


if __name__ == "__main__":
    main()
