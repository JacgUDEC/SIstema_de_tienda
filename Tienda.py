class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

    def mostrarinfo(self):
        return f"Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}"

class Tienda:
    def __init__(self):
        self.inventario=[]
    def agregar(self, producto):
        self.inventario.append(producto)
    def mostarinvent(self):
        print("\n🧰---Inventario---🧰\n")
        for i, producto in enumerate(self.inventario):
            print(f"{i+1}. {producto.mostrarinfo()}")
            
class Carro:
    def __init__(self):
        self.productos=[]
    def agregaralcarro(self, producto):
        if producto.stock > 0:
            self.productos.append(producto)
            producto.stock -= 1
            print("\nSe ha agragado el producto al carrito ☑️")
        else:
            print("No hay stock ❗")
    def mostrarcarrito(self):
        print("\n🛒---Carro---🛒\n")
        for w in self.productos:
            print(f"▫️ {w.nombre} -- {w.precio}")
    
    def calcular(self):
        total = sum(w.precio for w in self.productos)
        print(f"\nTotal: {total}")


def menuprinc():
    print("\n🏪---Tienda---🏪\n")
    print("1. Agregar productos al inventario")
    print("2. Agregar productos al carro")
    print("3. Ver carrito")
    print("4. Salir")


tienda=Tienda()
carro=Carro()


def agregaralatienda():
    print("\n📦---Agregar al inventario---📦")
    nombre=input("\nNombre: ")
    precio=int(input("Precio: "))
    stock=int(input("Stock: "))
    return Producto(nombre, precio, stock)


while True:
    menuprinc()
    opc = int(input("\n> "))

    if opc==1:
        p=agregaralatienda()
        tienda.agregar(p)
        print("\nProducto agregado ☑️")
    elif opc==2:
        tienda.mostarinvent()
        while True:
            try:
                pc=int(input("\n> "))

                if 1 <= pc <= len(tienda.inventario):
                    carro.agregaralcarro(tienda.inventario[pc-1])
                    break
                else:
                    tienda.mostarinvent()
                    print("\nProducto no existe🚫")

            except:
                tienda.mostarinvent()
                print("\nDebes escribir un número⚠️")
    elif opc==3:
        carro.mostrarcarrito()
        carro.calcular()
    elif opc==4:
        break
    else:
        print("opcion no valida❗")