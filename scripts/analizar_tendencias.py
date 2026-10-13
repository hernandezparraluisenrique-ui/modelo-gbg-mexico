
import csv
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO = RAIZ / "serie_mensual_analisis.csv"

with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivo:
    filas = list(csv.DictReader(archivo))

for hospedador in ("bovinos", "porcinos"):
    datos = [
        (fila["periodo"], int(fila[hospedador]))
        for fila in filas
        if fila[hospedador] != ""
    ]

    print(f"\n--- {hospedador.upper()} ---")
    print(f"Meses válidos: {len(datos)}")
    print(f"Casos acumulados en meses válidos: {sum(valor for _, valor in datos)}")

    if datos:
        periodo_maximo, casos_maximos = max(datos, key=lambda x: x[1])
        print(f"Máximo mensual: {casos_maximos} casos en {periodo_maximo}")

        print("\nEvolución mensual:")
        for periodo, casos in datos:
            print(f"{periodo}: {casos}")
