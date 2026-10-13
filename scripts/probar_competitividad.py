
import sys
from pathlib import Path
import numpy as np

raiz_proyecto = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(raiz_proyecto))

from src.simulacion.simulador import ejecutar_simulacion

# Parámetros artificiales: todavía no son valores validados
parametros_base = {
    "b": 0.1,
    "muM": 0.1,
    "muF": 0.1,
    "mus": 1 / 7,
    "c": 1.0,
    "R": lambda t: 0.0
}

estado_inicial = [10000, 10000, 0]
tiempo = np.linspace(0, 30, 301)

# Liberaciones hipotéticas de machos estériles por día
liberaciones = [0, 250, 500, 1000, 2000]

resultados = {}

for liberacion in liberaciones:
    parametros = parametros_base.copy()
    parametros["R"] = lambda t, cantidad=liberacion: float(cantidad)

    resultado = ejecutar_simulacion(
        parametros,
        estado_inicial,
        tiempo
    )

    resultados[liberacion] = resultado.y[1, -1]

hembras_sin_liberacion = resultados[0]

print("\nLiberación diaria | Hembras al día 30 | Reducción frente a cero")
for liberacion, hembras in resultados.items():
    if hembras_sin_liberacion > 0:
        reduccion = 100 * (
            1 - hembras / hembras_sin_liberacion
        )
    else:
        reduccion = 0.0

    print(
        f"{liberacion:16d} | "
        f"{hembras:17.2f} | "
        f"{reduccion:22.2f}%"
    )
