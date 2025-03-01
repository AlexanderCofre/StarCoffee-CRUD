from CLASES.persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, rut, telefono, contraseña, fecha):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.rut = rut
        self.telefono = telefono
        self.contraseña = contraseña
        self.fecha = fecha
        self.prodcuto_comprado = [] # Lista de productos comprados

    # Metodo STR
    def __str__(self):
        return f"""
            Fecha\t{super()._Personafecha}
            Nombre\t{self.nombre}
            Apellido\t{self.apellido}
            Edad\t{self.edad}
            Rut\t{self.rut}
            Telefono\t{self.telefono}
        """