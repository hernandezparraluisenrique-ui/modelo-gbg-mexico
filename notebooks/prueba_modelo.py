import sys
from pathlib import Path

import numpy as np


# =========================================
# RUTA DEL PROYECTO
# =========================================

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from src.simulacion.simulador import ejecutar_simulacion


# =========================================
# PARÁMETROS PROVISIONALES
# =========================================


#parametros = {
 #   "rM": 0.5,
  #  "rF": 0.5,
   # "b": 10,
    #"a": 1.0,
    #"muM": 0.1,
    #"muF": 0.1,
   # "mus": 0.1,
   # "c": 0.8,
   # "R": 0
#}

parametros = {
    "b": 0.25,
    "muM": 0.1,
    "muF": 0.1,
    "mus": 0.1,
    "c": 0.8,
    "R": 0
}


# =========================================
# CONDICIONES INICIALES
# =========================================

#estado_inicial = [
   # 100,   # Mw - machos silvestres
   # 100,   # Fv - hembras vírgenes
  #  0,     # Fm - hembras apareadas
 #   0      # Ms - machos estériles
#]

estado_inicial = [
    100,   # Mw - machos silvestres
    100,   # Fw - hembras silvestres
    0      # Ms - machos estériles
]


# =========================================
# TIEMPO DE SIMULACIÓN
# =========================================

tiempo = np.linspace(
    0,
    100,
    1001
)


# =========================================
# EJECUTAR SIMULACIÓN
# =========================================

resultado = ejecutar_simulacion(
    parametros,
    estado_inicial,
    tiempo
)


# =========================================
# MOSTRAR RESULTADOS
# =========================================

#print("Simulación terminada")

#print("\nEstado final:")

#print(f"Machos silvestres: {resultado.y[0, -1]}")
#print(f"Hembras vírgenes: {resultado.y[1, -1]}")
#print(f"Hembras apareadas: {resultado.y[2, -1]}")
#print(f"Machos estériles: {resultado.y[3, -1]}")

print("Simulación terminada")

print("\nEstado final:")

print(f"Machos silvestres: {resultado.y[0, -1]}")
print(f"Hembras silvestres: {resultado.y[1, -1]}")
print(f"Machos estériles: {resultado.y[2, -1]}")

