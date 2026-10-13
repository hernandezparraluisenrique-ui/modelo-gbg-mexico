
import csv
from pathlib import Path

# Ubicación del proyecto y del archivo de datos
RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO_ENTRADA = RAIZ / "resumen_mensual.csv"
ARCHIVO_SALIDA = RAIZ / "serie_mensual_analisis.csv"

with open(ARCHIVO_ENTRADA, "r", newline="", encoding="utf-8-sig") as archivo:
    lector = csv.DictReader(archivo)
    filas = list(lector)

columnas_salida = [
    "periodo",
    "bovinos",
    "porcinos",
    "bovinos_completo",
    "porcinos_completo",
]

with open(ARCHIVO_SALIDA, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=columnas_salida)
    escritor.writeheader()

    for fila in filas:
        escritor.writerow({
            "periodo": fila["periodo"],
            "bovinos": (
                fila["bovinos"]
                if fila["bovinos_completo"] == "si"
                else ""
            ),
            "porcinos": (
                fila["porcinos"]
                if fila["porcinos_completo"] == "si"
                else ""
            ),
            "bovinos_completo": fila["bovinos_completo"],
            "porcinos_completo": fila["porcinos_completo"],
        })

print("Serie de análisis generada correctamente.")
print(f"Meses procesados: {len(filas)}")
print(f"Archivo: {ARCHIVO_SALIDA}")
print("Los meses incompletos se conservan sin una suma engañosa.")


