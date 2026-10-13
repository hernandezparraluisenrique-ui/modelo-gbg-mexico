
import numpy as np


import sys
from pathlib import Path

import numpy as np

# Añadir la carpeta raíz del proyecto a la ruta de búsqueda de Python
raiz_proyecto = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(raiz_proyecto))

from src.simulacion.simulador import ejecutar_simulacion
from src.escenarios.escenarios import comparar_supervivencia

# Parámetros artificiales para comprobar que el código funciona
parametros = {
    "b": 0.1,
    "muM": 0.1,
    "muF": 0.1,
    "mus": 1 / 7,
    "c": 1.0,
    "R": lambda t: 1000.0
}

# Estado inicial: machos silvestres, hembras silvestres,
# machos estériles
estado_inicial = [10000, 10000, 0]

# Simular 30 días
tiempo = np.linspace(0, 30, 301)

# Probar una simulación
resultado = ejecutar_simulacion(
    parametros,
    estado_inicial,
    tiempo
)

print("¿Terminó correctamente?:", resultado.success)
print("Número de tiempos calculados:", len(resultado.t))
print("Estado final [Mw, Fw, Ms]:", resultado.y[:, -1])

# Comparar duraciones esperadas de vida hipotéticas
resultados = comparar_supervivencia(
    parametros,
    estado_inicial,
    tiempo,
    [3, 7, 10, 14]
)

print("\nComparación de escenarios:")
for vida_media, simulacion in resultados.items():
    machos_esteriles_finales = simulacion.y[2, -1]
    print(
        f"Duración esperada: {vida_media} días | "
        f"Machos estériles al final: "
        f"{machos_esteriles_finales:.2f}"
    )