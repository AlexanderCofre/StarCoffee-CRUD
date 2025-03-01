class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}"

    def actualizar_stock(self, cantidad):
        # Actualizar el stock del producto
        if cantidad >= 0:
            self.stock += cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def vender(self, cantidad):
        # Vender una cantidad del producto
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("No hay suficiente stock para completar la venta.")
