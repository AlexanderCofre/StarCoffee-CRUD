import mysql.connector

def conex():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Ajusta según corresponda
            database="prueba4",
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )

        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
            return conn

    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None
