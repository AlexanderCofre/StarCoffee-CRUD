import traceback
from tabulate import tabulate
import hashlib
from CONEX.conex import conex
import json

# Funcion que llama a una funcion de bases de datos para mostrar datos con select
def listUser(connection):
    try:
        if not connection.is_connected():
            connection.reconnect()

        cursor = connection.cursor()
        cursor.execute("SELECT identificador ,nombre, apellido, edad, rut, telefono, contrasena, fecha FROM cliente")
        result = cursor.fetchall()
        
        if result is not None:
            headers = ["Identificador", "Nombre", "Apellido", "Edad", "RUT", "Telefono", "Contraseña", "Fecha"]
            result_list = [list(row) for row in result]
            table = tabulate(result_list, headers=headers, tablefmt="pretty")
            print(table, "\n")
        else:
            print("No se pudieron recuperar los datos de la base de datos.")
            return

    except Exception as ex:
        connection.rollback()
        print(f"Error en ListarUsuario: {ex}")
        return None
    finally:
        if connection.is_connected():
            connection.close()


# Funcion que busca al usuario ingresado y muestra sus datos a traves de una consulta de bases de datos
def found(RUT, connection):
    sql = "SELECT identificador, nombre, apellido, edad, rut, telefono, contrasena, fecha FROM cliente WHERE rut = %s"
    try:
        if not connection.is_connected():
            connection.reconnect()

        cursor = connection.cursor()
        cursor.execute(sql, (RUT,))
        result = cursor.fetchone()

        if result is not None:
            headers = ["Identificador", "Nombre", "Apellido", "Edad", "RUT", "Telefono", "Contraseña", "Fecha"]
            result_list = [list(result)]
            table = tabulate(result_list, headers=headers, tablefmt="pretty")
            print(table, "\n")
        else:
            print("No se encontraron resultados para el usuario.")

        return result  # Devuelve los resultados de la consulta realizada
    except Exception as ex:
        print(traceback.print_exc())
        return None
    finally:
        if connection.is_connected():
            cursor.close()


# Funcion que permite agregar clientes a la base de datos con la funcion "INSERT" de la base de datos
def insert(nombre, apellido, edad, rut, telefono, contraseña, fecha, connection):
    sql = "INSERT INTO cliente (nombre, apellido, edad, rut, telefono, contrasena, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    try:
        if not connection.is_connected():
            connection.reconnect()

        cursor = connection.cursor()
        cursor.execute(sql, (nombre, apellido, edad, rut, telefono, contraseña, fecha))  # Pasa los valores como una tupla aquí
        connection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Datos ingresados correctamente.")
        else:
            print("No se realizaron cambios en la base de datos")
    except Exception as ex:
        connection.rollback()
        print(f"Error al insertar: {ex}")
    finally:
        if connection.is_connected():
            cursor.close()


# Esta funcion permite actualizar los datos de los clientes identificados por RUT
def updateRut(nombre, apellido, edad, rut, telefono, contraseña, encontrar_rut,connection):
    sql = "UPDATE cliente SET nombre = %s, apellido = %s, edad = %s, rut = %s, telefono = %s, contrasena = %s WHERE rut = %s"
    try:
        if not connection.is_connected():
            connection.reconnect()

        cursor = connection.cursor()
        cursor.execute(sql, (nombre, apellido, edad, rut, telefono, contraseña, encontrar_rut))
        filas = cursor.rowcount
        connection.commit() # Confirma actualizacion
        return filas # Devuelve el numero de filas afectadas
    except Exception as ex:
        connection.rollback()
        print(f"Error para actualizar: {ex}")
        return 0


# Esta funcion permite eliminar buscando por RUT
def deleteRut(RUT, connection):
    sql = "DELETE FROM cliente WHERE rut = %s"
    try:
        if not connection.is_connected():
            connection.reconnect()

        cursor = connection.cursor()
        cursor.execute(sql, (RUT,))
        connection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print(f"{filas} fila/s eliminadas")
        else:
            print("Usuario no encontrado")
    except Exception as ex:
        connection.rollback()
        print(f"Error en eliminar: {ex}")
    finally:
        if connection.is_connected():
            cursor.close()


# Funcion para calcular el hash MD5 
def enconde(contraseña):
    md5 = hashlib.md5(contraseña.encode())
    return md5.hexdigest()

# Funcion para verificar las credenciales del usuario
def verificar_credenciales(usuario, contraseña, connection):
    query = "SELECT nombre, contrasena FROM cliente WHERE nombre = %s"

    try:
        if not connection.is_connected():
            connection.reconnect()
        
        cursor = connection.cursor()
        cursor.execute(query, (usuario,))
        result = cursor.fetchone()

        if result is not None:
            contraseña_insertada = result[1]
            if enconde(contraseña) == contraseña_insertada:
                return True
            else:
                print("\x1b[1;31mContraseña Incorrecta.\x1b[0m")
        else:
            print("Usuario no encontrado.")

        return False
    except Exception as ex:
        print(f"\x1b[1;31mError al verificar credenciales: {ex}\x1b[0m")
        return False
    finally:
        if connection.is_connected():
            cursor.close


def prepararExportarJson():
    lista = []
    lista2 = []
    dic = {}
    c = conex()

    query = "SELECT identificador, nombre, apellido, edad, rut, telefono, contrasena, fecha FROM cliente"

    try:
        if not c.is_connected():
            c.reconnect()

        cursor = c.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        for u in result:
            clientes = (u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7])
            lista.append(clientes)

        for w in lista:
            lista2.append({"identificador": w[0], "nombre": w[1], "apellido": w[2], "edad": w[3], "rut": w[4], "telefono": w[5], "contrasena": w[6], "fecha": w[7]})
            dic["Datos"] = lista2
        else:
            print("No se encontraron resultados.")

        print("\x1b[1;32mExportacion Completa.\x1b[0m")
        exportarCliente("Clientes.json", dic)

    except Exception as ex:
        print(ex)

    return lista


def exportarCliente(archivo, obj):
    resu = {}
    try:
        out_file = open(archivo, "w", encoding="utf-8")
        json.dump(obj, out_file, indent=4)
        out_file.close()
        resu["mensaje"] = "\x1b[1;32mDatos Exportados Satisfactoriamente.\x1b[0m"

    except Exception as ex:
        resu["Error"] = ex

        
def leerJson():
    try:
        with open("Clientes.json") as file:
            data = json.load(file)

        for y in data["Datos"]:
            print(json.dumps(y, indent=4))
    
    except FileNotFoundError:
        # Error que se genera cuando no es posible encontrar el archivo
        print("Primero tiene que exportar al json.")
    except KeyError:
        # Error que se presenta cuando "Datos" no esta presente en el diccionario JSON
        print("\x1b[1;31El archivo JSON no contiene la variable 'Datos'.\x1b[0m")
    except json.JSONDecodeError:
        # Se lansa cuando hay un error al decodificar el archivo JSON.
        print("\x1b[1;31Error al decodificar el archivo JSON.\x1b[0m")


def importarClientesJson():
    lista = []

    try:
        with open("Clientes.json") as file:
            data = json.load(file)

        for x in data["Datos"]:
            lista.append((x["nombre"], x["apellido"], x["edad"], x["rut"], x["telefono"], x["contrasena"], x["fecha"]))

        query = "INSERT INTO cliente (nombre, apellido, edad, rut, telefono, contrasena, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        connection = conex()
        cursor = connection.cursor()
        cursor.executemany(query, lista)
        connection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("\x1b[1;32mDatos Agregados Satisfactoriamente.\x1b[0m")

        else:
            print("\x1b[1;31No se realizaron cambios.\x1b[0m")
    except Exception as ex:
        print("\x1b[1;31mError al insertar JSON\x1b[0m")