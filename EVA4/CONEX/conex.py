import mysql.connector
from mysql.connector import Error

def conex():
    try:
        myconn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="prueba4"
        )
        return myconn
    except Error as ex:
        print(f"Error de conexión: {ex}")
        return None