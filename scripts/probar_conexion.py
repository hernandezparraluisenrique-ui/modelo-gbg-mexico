
import mysql.connector

conexion = None

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Pasteldequeso1",
        database="gbg_mexico"
    )

    if conexion.is_connected():
        print("¡Conexión exitosa con MySQL!")
        print("Base de datos: gbg_mexico")

        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES")

        print("\nTablas encontradas:")
        for fila in cursor.fetchall():
            print("-", fila[0])

        cursor.close()

except mysql.connector.Error as error:
    print("No se pudo conectar con MySQL.")
    print("Detalle del error:", error)

finally:
    if conexion is not None and conexion.is_connected():
        conexion.close()
        print("\nConexión cerrada correctamente.")