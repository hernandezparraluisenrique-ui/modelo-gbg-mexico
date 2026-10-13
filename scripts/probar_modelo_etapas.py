
import numpy as np
from src.modelo.modelo_etapas import modelo_gbg_etapas

# Parámetros ficticios para comprobar el funcionamiento.
# NO son valores biológicos validados ni datos reales de la planta.
parametros = {
    "b": 0.1,
    "k_h": 1 / 2,
    "k_l": 1 / 5,
    "k_p": 1 / 7,

    "mu_h": 0.05,
    "mu_l": 0.05,
    "mu_p": 0.05,
    "mu_m": 0.1,
    "mu_f": 0.1,
    "mu_ps": 0.03,
    "mu_s": 1 / 7,

    "c": 1.0,
    "proporcion_machos": 0.5,

    # Ejemplo artificial: 1,000 pupas por día.
    "produccion_pupas": lambda t: 1000.0,

    "proporcion_sexado": 0.5,
    "proporcion_emergencia": 0.8,
    "proporcion_liberacion": 0.9,
}

# Orden: H, L, P, Mw, Fw, Ps, Ms
estado_inicial = [
    1000,  # Huevos silvestres
    500,   # Larvas silvestres
    200,   # Pupas silvestres
    1000,  # Machos silvestres
    1000,  # Hembras silvestres
    0,     # Pupas en proceso de planta
    0,     # Machos estériles en campo
]


from scipy.integrate import solve_ivp

tiempo = np.linspace(0, 30, 301)

resultado = solve_ivp(
    fun=lambda t, estado: modelo_gbg_etapas(
        t, estado, parametros
    ),
    t_span=(0, 30),
    y0=estado_inicial,
    t_eval=tiempo,
    method="RK45",
)

print("\nSimulación de 30 días")
print("---------------------")
print("¿Integración exitosa?:", resultado.success)
print("Mensaje:", resultado.message)

nombres = ["Huevos", "Larvas", "Pupas", "Machos silvestres",
           "Hembras silvestres", "Pupas de planta",
           "Machos estériles"]

if resultado.success:
    print("\nPoblaciones iniciales y finales:")
    for nombre, inicial, final in zip(
        nombres, estado_inicial, resultado.y[:, -1]
    ):
        print(
            f"{nombre}: inicial={inicial:.2f}, "
            f"final={final:.2f}"
        )

    print(
        "\nValor mínimo calculado entre todos los estados:",
        f"{resultado.y.min():.4f}"
    )
