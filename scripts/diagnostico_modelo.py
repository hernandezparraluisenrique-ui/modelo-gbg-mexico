
from copy import deepcopy

import numpy as np
from scipy.integrate import solve_ivp

from src.modelo.modelo_etapas import modelo_gbg_etapas
from src.modelo.parametros import PARAMETROS

ESTADO_INICIAL = [1000, 500, 200, 1000, 1000, 0, 0]
DIAS = 180


def ejecutar(nombre, cambios=None):
    parametros = deepcopy(PARAMETROS)
    parametros["produccion_pupas"] = lambda t: 0.0

    if cambios:
        parametros.update(cambios)

    tiempos = np.arange(DIAS + 1, dtype=float)
    resultado = solve_ivp(
        lambda t, y: modelo_gbg_etapas(t, y, parametros),
        (0, DIAS),
        ESTADO_INICIAL,
        t_eval=tiempos,
        rtol=1e-7,
        atol=1e-9,
    )

    if not resultado.success:
        raise RuntimeError(resultado.message)

    # Estados: huevos, larvas, pupas, machos silvestres,
    # hembras silvestres, pupas de planta, machos estériles.
    y = np.maximum(resultado.y, 0)
    print(f"\n{nombre}")
    print(f"Hembras silvestres al día 0: {y[4, 0]:.2f}")
    print(f"Hembras silvestres al día 30: {y[4, 30]:.2f}")
    print(f"Hembras silvestres al día 90: {y[4, 90]:.2f}")
    print(f"Hembras silvestres al día 180: {y[4, -1]:.2f}")
    print(f"Machos silvestres al día 180: {y[3, -1]:.2f}")


ejecutar("Parámetros actuales")
ejecutar("Reproducción duplicada", {"b": 0.2})
ejecutar("Mortalidad reducida", {
    "mu_h": 0.01,
    "mu_l": 0.01,
    "mu_p": 0.01,
    "mu_m": 0.03,
    "mu_f": 0.03,
})
