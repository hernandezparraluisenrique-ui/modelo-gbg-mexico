import numpy as np
from scipy.integrate import solve_ivp

from src.modelo.poblacion import modelo_gbg


def ejecutar_simulacion(parametros, estado_inicial, tiempo):
    """
    Ejecuta una simulación del modelo poblacional del GBG.

    Parámetros
    ----------
    parametros : dict
        Parámetros del modelo.

    estado_inicial : list
        Estado inicial:
        [Mw, Fv, Fm, Ms]

    tiempo : array
        Vector de tiempo de simulación.

    Retorna
    -------
    resultado : OdeResult
        Resultado de la simulación.
    """

    resultado = solve_ivp(
        fun=lambda t, estado: modelo_gbg(
            t,
            estado,
            parametros
        ),
        t_span=(tiempo[0], tiempo[-1]),
        y0=estado_inicial,
        t_eval=tiempo,
        method="RK45"
    )

    return resultado

