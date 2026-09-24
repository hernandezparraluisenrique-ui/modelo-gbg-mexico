import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# =========================================
# RUTA DEL PROYECTO
# =========================================

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from src.simulacion.simulador import ejecutar_simulacion


# =========================================
# PARÁMETROS DEL MODELO
# =========================================

parametros = {
    "b": 0.25,
    "muM": 0.1,
    "muF": 0.1,
    "mus": 0.1,
    "c": 0.8
}


# =========================================
# CONDICIONES INICIALES
# =========================================

estado_inicial = [
    100,   # Mw
    100,   # Fw
    0      # Ms
]


# =========================================
# TIEMPO DE SIMULACIÓN
# =========================================

# 100 semanas
# 1 punto cada 0.1 semanas

tiempo = np.linspace(
    0,
    100,
    1001
)


# =========================================
# FUNCIONES DE LIBERACIÓN
# =========================================

def liberacion_sin_tie(t):
    """
    Sin liberación de machos estériles.
    """
    return 0


def liberacion_programada(t):
    """
    Programa de liberación de machos estériles
    por semana.

    Semanas 0-9:   0 machos/semana
    Semanas 10-19: 20 machos/semana
    Semanas 20-29: 40 machos/semana
    Semana 30+:    60 machos/semana
    """

    if t < 10:
        return 0

    elif t < 20:
        return 20

    elif t < 30:
        return 40

    else:
        return 60


# =========================================
# ESCENARIO 1: SIN TIE
# =========================================

parametros_sin_tie = parametros.copy()

parametros_sin_tie["R"] = liberacion_sin_tie


resultado_sin_tie = ejecutar_simulacion(
    parametros_sin_tie,
    estado_inicial,
    tiempo
)


# =========================================
# ESCENARIO 2: CON TIE
# =========================================

parametros_con_tie = parametros.copy()

parametros_con_tie["R"] = liberacion_programada


resultado_con_tie = ejecutar_simulacion(
    parametros_con_tie,
    estado_inicial,
    tiempo
)


# =========================================
# POBLACIÓN SILVESTRE TOTAL
# =========================================

poblacion_sin_tie = (
    resultado_sin_tie.y[0]
    + resultado_sin_tie.y[1]
)


poblacion_con_tie = (
    resultado_con_tie.y[0]
    + resultado_con_tie.y[1]
)


# =========================================
# LIBERACIÓN PROGRAMADA
# =========================================

liberaciones = [
    liberacion_programada(t)
    for t in tiempo
]


# =========================================
# RESULTADOS FINALES
# =========================================

print("=========================================")
print("ESCENARIO SIN TIE")
print("=========================================")

print(
    f"Machos silvestres: "
    f"{resultado_sin_tie.y[0, -1]}"
)

print(
    f"Hembras silvestres: "
    f"{resultado_sin_tie.y[1, -1]}"
)

print(
    f"Población silvestre total: "
    f"{poblacion_sin_tie[-1]}"
)


print("\n=========================================")
print("ESCENARIO CON TIE")
print("=========================================")

print(
    f"Machos silvestres: "
    f"{resultado_con_tie.y[0, -1]}"
)

print(
    f"Hembras silvestres: "
    f"{resultado_con_tie.y[1, -1]}"
)

print(
    f"Machos estériles: "
    f"{resultado_con_tie.y[2, -1]}"
)

print(
    f"Población silvestre total: "
    f"{poblacion_con_tie[-1]}"
)


# =========================================
# GRÁFICA COMPARATIVA
# =========================================

plt.figure(figsize=(10, 6))


# Población silvestre sin TIE
plt.plot(
    tiempo,
    poblacion_sin_tie,
    label="Sin TIE"
)


# Población silvestre con TIE
plt.plot(
    tiempo,
    poblacion_con_tie,
    label="Con TIE"
)


# Liberación programada
plt.plot(
    tiempo,
    liberaciones,
    label="Liberación de estériles"
)


plt.xlabel("Tiempo (semanas)")

plt.ylabel("Población / liberación")

plt.title(
    "Dinámica de la población del GBG y liberación programada"
)


plt.legend()

plt.grid()

plt.tight_layout()

plt.show()