
from pathlib import Path
import numpy as np
import pandas as pd

archivo = Path("resultados_liberaciones/trayectorias_liberaciones.csv")

if not archivo.exists():
    raise FileNotFoundError(
        f"No se encontró {archivo}. "
        "Ejecuta primero: python -m scripts.simular_liberaciones"
    )

df = pd.read_csv(archivo)

print("VALIDACIÓN DE LAS SIMULACIONES DE LIBERACIÓN")
print("\nColumnas:", list(df.columns))
print("Filas:", len(df))

# Detectar datos faltantes o infinitos en columnas numéricas.
numericos = df.select_dtypes(include="number")

assert not numericos.empty, "No hay columnas numéricas."
assert np.isfinite(numericos.to_numpy()).all(), (
    "Hay valores NaN o infinitos."
)

# Identificar las columnas de poblaciones.
columnas_poblacion = [
    c for c in df.columns
    if any(x in c.lower() for x in
           ["hembra", "macho", "larva", "huevo", "pupa"])
]

for columna in columnas_poblacion:
    minimo = df[columna].min()
    print(f"Mínimo de {columna}: {minimo:.6f}")
    assert minimo >= -1e-6, (
        f"Se detectaron valores negativos en {columna}."
    )

print("\nOK: no hay valores faltantes o infinitos "
      "en las columnas numéricas.")
print("OK: las poblaciones identificadas no son negativas.")
print(
    "\nNota: estas pruebas verifican consistencia numérica; "
    "no validan el modelo frente a datos biológicos reales."
)


