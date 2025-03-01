from producto import Producto

# Almacen donde se almacenaran los productos
class Almacen:
    productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)


# Crear una instancia de la Cafetería
almacen = Almacen()

# Agregar productos
cafe_expreso = Producto("Café Expreso", 700, 100)
cafe_capuccino = Producto("Café Cappuccino", 1000, 50)
cafe_latte = Producto("Café Latte", 1250, 75)
cafe_mocha = Producto("Café Mocha", 1500, 60)
te_verde = Producto("Té Verde", 500, 120)
te_negro = Producto("Té Negro", 500, 100)

# Se agregan los productos creados a la lista
almacen.agregar_producto(cafe_expreso)
almacen.agregar_producto(cafe_capuccino)
almacen.agregar_producto(cafe_latte)
almacen.agregar_producto(cafe_mocha)
almacen.agregar_producto(te_verde)
almacen.agregar_producto(te_negro)