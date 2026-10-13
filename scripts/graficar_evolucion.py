
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Ubicación del archivo CSV
CARPETA_PROYECTO = Path(__file__).resolve().parent.parent
archivo_csv = CARPETA_PROYECTO / "resumen_mensual.csv"

# Leer datos
datos = pd.read_csv(archivo_csv)
datos["mes"] = pd.to_datetime(datos["mes"])
datos["suma_valores_numericos"] = pd.to_numeric(
    datos["suma_valores_numericos"], errors="coerce"
)

# Organizar sumas y número de registros numéricos
sumas = datos.pivot(
    index="mes",
    columns="hospedador",
    values="suma_valores_numericos"
)

conteos = datos.pivot(
    index="mes",
    columns="hospedador",
    values="registros_numericos"
)

# Crear dos gráficas
fig, ejes = plt.subplots(2, 1, figsize=(13, 9), sharex=True)

# Gráfica 1: sumas de valores numéricos
for hospedador in sumas.columns:
    ejes[0].plot(
        sumas.index,
        sumas[hospedador],
        marker="o",
        label=hospedador
    )

ejes[0].set_title("Suma mensual de valores numéricos registrados")
ejes[0].set_ylabel("Suma de valores")
ejes[0].legend(title="Hospedador")
ejes[0].grid(True, alpha=0.3)

# Gráfica 2: cantidad de registros numéricos
for hospedador in conteos.columns:
    ejes[1].plot(
        conteos.index,
        conteos[hospedador],
        marker="o",
        label=hospedador
    )

ejes[1].set_title("Cantidad de registros numéricos por mes")
ejes[1].set_ylabel("Número de registros")
ejes[1].set_xlabel("Mes")
ejes[1].legend(title="Hospedador")
ejes[1].grid(True, alpha=0.3)

# Mostrar etiquetas cada tres meses
ejes[1].xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ejes[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.xticks(rotation=45)

plt.tight_layout()

# Guardar imagen
salida = CARPETA_PROYECTO / "evolucion_mensual.png"
plt.savefig(salida, dpi=200, bbox_inches="tight")
plt.show()

print(f"Gráfica guardada en: {salida}")