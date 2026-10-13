
import csv
from pathlib import Path
from collections import defaultdict

carpeta_proyecto = Path(__file__).resolve().parent.parent
archivo_csv = carpeta_proyecto / "datos_importacion.csv"

resumen = defaultdict(lambda: {
    "numericos": 0,
    "guiones": 0,
    "vacios": 0,
    "suma_numerica": 0
})

celdas_vacias = []

with open(archivo_csv, "r", encoding="utf-8-sig", newline="") as archivo:
    lector = csv.DictReader(archivo)

    for registro in lector:
        hospedador = registro["hospedador"]
        tipo = registro["estado_registro"]

        if tipo == "numerico":
            clave = "numericos"
        elif tipo == "guion":
            clave = "guiones"
        elif tipo == "vacio":
            clave = "vacios"
        else:
            raise ValueError(f"Tipo de registro desconocido: {tipo}")
        resumen[hospedador][clave] += 1

        if tipo == "numerico":
            resumen[hospedador]["suma_numerica"] += int(
                registro["valor_numerico"]
            )

        if tipo == "vacio":
            celdas_vacias.append((
                registro["nombre_estado"],
                hospedador,
                registro["periodo"]
            ))

print("RESUMEN POR HOSPEDADOR")
for hospedador, datos in sorted(resumen.items()):
    print(f"\n{hospedador}:")
    print(f"  Numéricos: {datos['numericos']}")
    print(f"  Guiones: {datos['guiones']}")
    print(f"  Celdas vacías: {datos['vacios']}")
    print(f"  Suma de valores numéricos: {datos['suma_numerica']}")

print("\nCELDAS VACÍAS ENCONTRADAS")
for estado, hospedador, periodo in celdas_vacias:
    print(f"  {estado} | {hospedador} | {periodo}")

print("\nVerificación terminada. No se modificó ningún archivo.")
