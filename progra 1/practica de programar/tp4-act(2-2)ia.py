# Lista vacía para guardar productos
productos = []

# 1. Pedir al usuario que ingrese 5 productos
for i in range(5):
    producto = input("Ingrese un producto: ")
    productos.append(producto)

# 2. Mostrar la lista ordenada alfabéticamente
print("\nLista ordenada alfabéticamente:")
print(sorted(productos))

# 3. Preguntar qué producto desea eliminar
eliminar = input("\n¿Qué producto desea eliminar?: ")

# 4. Eliminar el producto si está en la lista
if eliminar in productos:
    productos.remove(eliminar)
    print("\nProducto eliminado correctamente.")
else:
    print("\nEse producto no está en la lista.")

# Mostrar la lista actualizada
print("\nLista actualizada:")
print(productos)
