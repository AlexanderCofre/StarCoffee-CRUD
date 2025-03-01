from CRUD.crud import listUser, found, insert, updateRut, deleteRut, enconde, verificar_credenciales, leerJson, importarClientesJson, prepararExportarJson
from CONEX.conex import conex
from datetime import datetime
from CLASES.cliente import Cliente

def menu_general():
    while True:
        print("\x1b[1;32mBienvenido a STARCOFFE\x1b[0m")
        print("1.- Gestion de Clientes")
        print("2.- Gestion de JSON")
        print("3.- Salir")
        opc = input("Ingrese una opcion: ")
        print("")

        if opc == "1":
            menu_usuario()
        elif opc == "2":
            menu_json()
        elif opc == "3":
            print("\x1b[1;31mSaliendo... Hasta Luego\x1b[0m")
            break
        else:
            print("Ingrese 1 a 3.")


def menu_usuario():
    connection = conex()

    try:
        while True:
            print("\n1.- Listar Clientes")
            print("2.- Mostrar Usuarios por su rut")
            print("3.- Agregar Cliente")
            print("4.- Actualizar Cliente")
            print("5.- Eliminar Cliente")
            print("6.- Salir")
            opc = input("Ingrese una opcion: ")

            if opc == "1":
                print("Listando Clientes...\n")
                listUser(connection)
            elif opc == "2":
                print("Buscando por RUT...\n")
                rut = input("Ingrese el rut del cliente a encontrar: ")
                found(rut, connection)
            elif opc == "3":
                print("Agregando Clientes...\n")
                nombre = input("Ingrese el nombre del cliente: ")
                apellido = input("Ingrese el apellido del cliente: ")
                while True:
                    try:
                        edad = int(input("Ingrese la edad del cliente: "))
                        if 16 <= edad <= 100:
                            break
                        else:
                            print("Ingrese una edad entre 16 y 100")
                    except ValueError:
                        print("Ingrese un valor entero")
                rut = input("Ingrese el rut del cliente: ")
                while True:
                    try:
                        telefono = int(input("Ingrese el teléfono del cliente (8 dígitos): "))
                        if len(str(telefono)) == 8:
                            break
                        else:
                            print("Ingrese un número telefónico válido (debe tener 8 dígitos).")
                    except ValueError:
                        print("Ingrese un número válido.")
                contraseña = input("Ingrese la contraseña del cliente: ")
                contraseña = enconde(contraseña)
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    

                c = Cliente(nombre, apellido, edad, rut, telefono, contraseña, fecha)
                insert(c.nombre, c.apellido, c.edad, c.rut, c.telefono, c.contraseña, c.fecha, connection)
            elif opc == "4":
                encontrar_rut = input("Ingrese el rut del cliente a actualizar: ")
                cliente = found(encontrar_rut, connection)

                if cliente is not None:
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    while True:
                        try:
                            edad = int(input("Ingrese la edad del cliente: "))
                            if 16 <= edad <= 100:
                                break
                            else:
                                print("Ingrese una edad entre 16 y 100")
                        except ValueError:
                            print("Ingrese un valor entero")
                    rut = input("Ingrese el rut: ")
                    while True:
                        try:
                            telefono = int(input("Ingrese el teléfono del cliente (8 dígitos): "))
                            if len(str(telefono)) == 8:
                                break
                            else:
                                print("Ingrese un número telefónico válido (debe tener 8 dígitos).")
                        except ValueError:
                            print("Ingrese un número válido.")
                    contraseña = input("Ingrese la contraseña: ")
                    contraseña = enconde(contraseña)  

                    resumen = updateRut(nombre, apellido, edad, rut, telefono, contraseña, encontrar_rut, connection)

                    if resumen > 0:
                        print(f"{resumen} fila/as actualizadas correctamente")
                    else:
                        print("No se han podido realizar cambios.")

                else:
                    print("Usuario no encontrado.")
            elif opc == "5":
                rut = input("Ingrese el rut del cliente a eliminar: ")
                cliente = found(rut, connection)

                if cliente is not None:
                    deleteRut(rut, connection)

            elif opc == "6":
                print("\x1b[1;31mSaliendo del Apartado.\x1b[0m\n")
                break
            else:
                print("Ingrese de 1 a 6.")
        
    finally:
        if connection.is_connected():
            connection.close()


def menu_json():
    try:
        while True:
            print("1.- Leer Archivos JSON.")
            print("2.- Importar a JSON.")
            print("3.- Exportar a JSON.")
            print("4.- Salir.")

            opc = input("\n Ingrese una opcion: ")
            print("")

            if opc == "1":
                print("Leer datos de JSON existentes...")
                leerJson()
            elif opc == "2":
                print("Preparando importacion desde JSON hacia la BD...")
                importarClientesJson()
            elif opc == "3":
                print("Exportando a JSON...")
                prepararExportarJson()
            elif opc == "4":
                print("\x1b[1;31mSaliendo del Apartado.\x1b[0m\n")
                break
            else:
                print("\033[93mOpcion no valida.\033[0m")
    except Exception as ex:
        print(ex)


def login():
    connection = conex()

    intentos_maximos = 3
    intentos = 0
    print("Ingrese el nombre y la contraseña correcta para ingresar.")
    while intentos < intentos_maximos:
        nombre_usuario = input("Ingrese su nombre de usuario: ").lower()
        contraseña = input("Ingrese su contraseña: ")

        if verificar_credenciales(nombre_usuario, contraseña, connection):
            print("\x1b[1;32mInicio de sesión exitoso.\x1b[0m\n")
            menu_general()
            break
        else:
            intentos += 1
            print(f"\033[93mInicio de sesión fallido. Intentos restantes: {intentos_maximos - intentos}\033[0m")
    if intentos == intentos_maximos:
        print("\x1b[1;31mNúmero maximo de intentos alcanzados.\n\n CERRANDO PROGRAMA.\x1b[0m")
