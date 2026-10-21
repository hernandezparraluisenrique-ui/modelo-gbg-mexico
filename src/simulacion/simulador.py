
import numpy as np
from scipy.integrate import solve_ivp



from src.modelo.poblacion import modelo_gbg
from src.modelo.modelo_etapas import modelo_gbg_etapas


def ejecutar_simulacion(
    parametros,
    estado_inicial,
    tiempo,
    modelo="original",
):
    tiempo = np.asarray(tiempo, dtype=float)
    estado_inicial = np.asarray(estado_inicial, dtype=float)

    if tiempo.ndim != 1 or len(tiempo) < 2:
        raise ValueError(
            "tiempo debe contener al menos dos puntos."
        )

    if not np.all(np.isfinite(tiempo)):
        raise ValueError("tiempo debe contener valores finitos.")

    if np.any(np.diff(tiempo) <= 0):
        raise ValueError(
            "tiempo debe estar ordenado y sin repetidos."
        )

    if not np.all(np.isfinite(estado_inicial)):
        raise ValueError(
            "estado_inicial debe contener valores finitos."
        )

    if np.any(estado_inicial < 0):
        raise ValueError(
            "estado_inicial no puede tener valores negativos."
        )

    if modelo == "original":
        funcion_modelo = modelo_gbg
    elif modelo == "etapas":
        funcion_modelo = modelo_gbg_etapas
    else:
        raise ValueError(
            "modelo debe ser 'original' o 'etapas'."
        )

    
    resultado = solve_ivp(
        fun=lambda t, estado: funcion_modelo(
            t, estado, parametros
        ),
        t_span=(tiempo[0], tiempo[-1]),
        y0=estado_inicial,
        t_eval=tiempo,
        method="RK45",
        rtol=1e-7,
        atol=1e-9,
    )

    if not resultado.success:
        raise RuntimeError(resultado.message)

    if not np.all(np.isfinite(resultado.y)):
        raise RuntimeError(
            "La simulación produjo resultados no finitos."
        )

    # Detectar valores negativos relevantes.
    tolerancia_negativa = 1e-7

    if np.any(resultado.y < -tolerancia_negativa):
        minimo = float(np.min(resultado.y))
        raise RuntimeError(
            f"La simulación produjo poblaciones negativas "
            f"significativas. Mínimo: {minimo:.8g}. "
            "Revisa las ecuaciones y los parámetros."
        )

    # Corregir únicamente residuos negativos muy pequeños
    # atribuibles a la precisión numérica.
    resultado.y[resultado.y < 0] = 0.0

    return resultado

