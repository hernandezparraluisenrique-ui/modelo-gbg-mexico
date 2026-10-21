
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Ubicación del proyecto y archivo de datos
BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_CSV = BASE_DIR / "resumen_mensual.csv"

df = pd.read_csv(ARCHIVO_CSV, dtype={"periodo": str})

# Convertir los casos a valores numéricos
df["bovinos"] = pd.to_numeric(df["bovinos"], errors="coerce")
df["porcinos"] = pd.to_numeric(df["porcinos"], errors="coerce")
# No graficar como definitivos los totales bovinos incompletos
df.loc[df["bovinos_completo"] == "no", "bovinos"] = float("nan")

# Mostrar las sumas mensuales registradas
print("Casos mensuales registrados:")
print(df[["periodo", "bovinos", "porcinos",
          "bovinos_completo", "porcinos_completo"]].to_string(index=False))

# Crear la gráfica
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    df["periodo"],
    df["bovinos"],
    marker="o",
    label="Bovinos",
)

ax.plot(
    df["periodo"],
    df["porcinos"],
    marker="s",
    label="Porcinos",
)

ax.set_title("Casos mensuales de GBG registrados en México")
ax.set_xlabel("Mes")
ax.set_ylabel("Casos registrados")
ax.tick_params(axis="x", rotation=60)
ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()

archivo_imagen = BASE_DIR / "evolucion_casos_observados.png"
fig.savefig(archivo_imagen, dpi=150)
plt.close(fig)

print(f"\nGráfica guardada en: {archivo_imagen}")
