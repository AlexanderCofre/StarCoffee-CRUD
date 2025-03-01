# StarCoffee CRUD System

¡Bienvenido al sistema de gestión de clientes para StarCoffee!  
Este proyecto proporciona una interfaz de línea de comandos para gestionar clientes de una cafetería,
permitiendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y la exportación/importación de datos en formato JSON.

## Características
- **Gestión de Clientes**: Agregar, actualizar, eliminar y listar clientes.
- **Exportación/Importación JSON**: Exportar e importar datos de clientes en formato JSON.
- **Seguridad**: Hashing de contraseñas para proteger la información de los usuarios.
- **Interfaz de Línea de Comandos**: Menú interactivo para facilitar la gestión de clientes.

## Requisitos
- Python 3.x
- MySQL
- Librerías de Python: `mysql-connector-python`, `tabulate`

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/StarCoffee-CRUD.git
   cd StarCoffee-CRUD
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura la base de datos MySQL:
   - Crea una base de datos llamada `prueba4`.
   - Asegúrate de que el usuario `root` no tenga contraseña o actualiza las credenciales en el archivo `conex.py`.

## Uso
1. Ejecuta el archivo `main.py`:
   ```bash
   python main.py
   ```
2. Sigue las instrucciones en el menú interactivo para gestionar los clientes.

## Estructura del Proyecto
- `CRUD/`: Contiene las funciones CRUD para gestionar los clientes.
- `CONEX/`: Contiene la configuración de conexión a la base de datos.
- `CLASES/`: Contiene las clases utilizadas en el proyecto.
- `MENU/`: Contiene los menús interactivos para la gestión de clientes y JSON.
- `main.py`: Punto de entrada del programa.
  
