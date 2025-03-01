# Zona de Importacion
from datetime import datetime

# Clase Padre
class Persona:
    # Le damos formato de hora
    fecha = ""
    nombre = ""
    apellido = ""
    edad = 0
    rut = ""

    # Definicion del metodo STR
    def __str__(self):
        return f"""
        Fecha\t{self.fecha}
        Nombre\t{self.nombre}
        Apellido\t{self.apellido}
        Edad\t{self.edad}
        Rut\t{self.rut}
        """