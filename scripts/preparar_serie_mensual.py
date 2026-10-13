
import csv
import mysql.connector
from pathlib import Path

# Ubicación del proyecto y archivo de salida
raiz_proyecto = Path(__file__).resolve().parent.parent
archivo_salida = raiz_proyecto / "resumen_mensual.csv"

conexion = None
cursor = None

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Pasteldequeso1",
        database="gbg_mexico"
    )

    cursor = conexion.cursor()

    consulta = """
        SELECT
            periodo,
            id_hospedador,
            SUM(
                CASE
                    WHEN estado_registro = 'numerico'
                    THEN valor_numerico
                    WHEN estado_registro = 'guion'
                    THEN 0
                    ELSE NULL
                END
            ) AS suma_casos,
            SUM(
                CASE WHEN estado_registro = 'vacio'
                THEN 1 ELSE 0 END
            ) AS cantidad_vacios,
            SUM(
                CASE WHEN estado_registro = 'numerico'
                THEN 1 ELSE 0 END
            ) AS cantidad_numericos,
            SUM(
                CASE WHEN estado_registro = 'guion'
                THEN 1 ELSE 0 END
            ) AS cantidad_guiones
        FROM casos_mensuales
        GROUP BY periodo, id_hospedador
        ORDER BY periodo, id_hospedador
    """

    cursor.execute(consulta)
    filas = cursor.fetchall()

    # Agrupar los resultados por mes
    meses = {}

    for periodo, hospedador, suma, vacios, numericos, guiones in filas:
        mes = periodo.strftime("%Y-%m")

        if mes not in meses:
            meses[mes] = {
                "bovinos": 0,
                "porcinos": 0,
                "bovinos_vacios": 0,
                "porcinos_vacios": 0,
                "bovinos_numericos": 0,
                "porcinos_numericos": 0,
                "bovinos_guiones": 0,
                "porcinos_guiones": 0,
            }

        nombre = "bovinos" if hospedador == 1 else "porcinos"

        meses[mes][nombre] = suma or 0
        meses[mes][f"{nombre}_vacios"] = vacios
        meses[mes][f"{nombre}_numericos"] = numericos
        meses[mes][f"{nombre}_guiones"] = guiones

    columnas = [
        "periodo",
        "bovinos",
        "porcinos",
        "bovinos_vacios",
        "porcinos_vacios",
        "bovinos_numericos",
        "porcinos_numericos",
        "bovinos_guiones",
        "porcinos_guiones",
        "bovinos_completo",
        "porcinos_completo",
    ]

    with open(
        archivo_salida,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()

        for mes, datos in sorted(meses.items()):
            fila = {"periodo": mes, **datos}

            for nombre in ("bovinos", "porcinos"):
                fila[f"{nombre}_completo"] = (
                    "si" if datos[f"{nombre}_vacios"] == 0 else "no"
                )

            escritor.writerow(fila)

    print("Serie mensual generada correctamente.")
    print(f"Archivo: {archivo_salida}")
    print(f"Meses procesados: {len(meses)}")

except mysql.connector.Error as error:
    print("Error al consultar MySQL:", error)

finally:
    if cursor is not None:
        cursor.close()

    if conexion is not None and conexion.is_connected():
        conexion.close()
