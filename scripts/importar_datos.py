
import csv
from pathlib import Path
import mysql.connector

# Archivos del proyecto
carpeta_proyecto = Path(__file__).resolve().parent.parent
archivo_csv = carpeta_proyecto / "datos_importacion.csv"

if not archivo_csv.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo: {archivo_csv}"
    )

# Leer y validar el CSV antes de conectarse a MySQL
with open(archivo_csv, "r", encoding="utf-8-sig", newline="") as archivo:
    lector = csv.DictReader(archivo)
    registros_csv = list(lector)

if len(registros_csv) != 1472:
    raise ValueError(
        f"Se esperaban 1472 registros, pero hay {len(registros_csv)}. "
        "No se importó nada."
    )

claves = set()

for r in registros_csv:
    clave = (r["nombre_estado"], r["hospedador"], r["periodo"])

    if clave in claves:
        raise ValueError(f"Registro duplicado en el CSV: {clave}")

    claves.add(clave)

    tipo = r["estado_registro"]
    original = r["valor_original"]
    numerico = r["valor_numerico"]

    if tipo == "numerico":
        if not numerico.isdigit() or int(numerico) < 0:
            raise ValueError(f"Valor numérico inválido: {r}")

    elif tipo == "guion":
        if original != "-" or numerico != "":
            raise ValueError(f"Registro de guion inválido: {r}")

    elif tipo == "vacio":
        if original != "" or numerico != "":
            raise ValueError(f"Registro vacío inválido: {r}")

    else:
        raise ValueError(f"Tipo de registro desconocido: {r}")

# Conexión a MySQL: usa los mismos datos de probar_conexion.py
conexion = None

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Pasteldequeso1",
        database="gbg_mexico"
    )

    cursor = conexion.cursor()

    # Confirmar que no haya una importación previa
    cursor.execute("SELECT COUNT(*) FROM casos_mensuales")
    total_actual = cursor.fetchone()[0]

    if total_actual != 0:
        raise RuntimeError(
            f"La tabla casos_mensuales ya contiene {total_actual} registros. "
            "Se cancela la importación para evitar duplicados."
        )

    # Insertar los estados sin duplicar los que ya existan
    estados = sorted({r["nombre_estado"] for r in registros_csv})

    cursor.executemany(
        "INSERT IGNORE INTO estados (nombre) VALUES (%s)",
        [(estado,) for estado in estados]
    )

    cursor.execute("SELECT id_estado, nombre FROM estados")
    ids_estados = {nombre: id_estado for id_estado, nombre in cursor.fetchall()}

    cursor.execute("SELECT id_hospedador, nombre FROM hospedadores")
    ids_hospedadores = {
        nombre: id_hospedador
        for id_hospedador, nombre in cursor.fetchall()
    }

    # Comprobar que todos los estados y hospedadores existen
    if not set(estados).issubset(ids_estados):
        raise ValueError("Falta algún estado en el catálogo de MySQL.")

    hospedadores_csv = {r["hospedador"] for r in registros_csv}

    if not hospedadores_csv.issubset(ids_hospedadores):
        raise ValueError(
            "Falta algún hospedador en MySQL. "
            f"Encontrados: {sorted(ids_hospedadores)}"
        )

    # Preparar las filas para casos_mensuales
    filas_mysql = []

    for r in registros_csv:
        valor_numerico = (
            int(r["valor_numerico"])
            if r["estado_registro"] == "numerico"
            else None
        )

        filas_mysql.append((
            ids_estados[r["nombre_estado"]],
            ids_hospedadores[r["hospedador"]],
            r["periodo"],
            r["valor_original"],
            valor_numerico,
            r["estado_registro"]
        ))

    # Insertar los 1472 registros dentro de una transacción
    cursor.executemany(
        """
        INSERT INTO casos_mensuales
        (id_estado, id_hospedador, periodo,
         valor_original, valor_numerico, estado_registro)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        filas_mysql
    )

    # Confirmar los cambios solo si todo salió bien
    conexion.commit()

    cursor.execute("SELECT COUNT(*) FROM estados")
    total_estados = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM casos_mensuales")
    total_registros = cursor.fetchone()[0]

    cursor.execute("""
        SELECT estado_registro, COUNT(*)
        FROM casos_mensuales
        GROUP BY estado_registro
        ORDER BY estado_registro
    """)
    resumen = cursor.fetchall()

    print("¡Importación completada correctamente!")
    print(f"Estados en la base de datos: {total_estados}")
    print(f"Registros mensuales importados: {total_registros}")
    print("\nResumen de registros:")
    for tipo, cantidad in resumen:
        print(f"  {tipo}: {cantidad}")

except Exception as error:
    if conexion is not None and conexion.is_connected():
        conexion.rollback()

    print("La importación no se completó.")
    print("Se revirtieron los cambios de esta transacción.")
    print("Detalle:", error)

finally:
    if conexion is not None and conexion.is_connected():
        conexion.close()