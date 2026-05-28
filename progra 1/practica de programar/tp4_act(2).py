productos = []

for i in range(5):
    producto = input("Ingrese un producto: ")
    productos.append(producto)


print("Lista actualizada: ")
print(sorted(productos))


eliminar = input("que producto desea eliminar?: ")

if eliminar in productos:
    productos.remove(eliminar)

print("lista actualizada")
print(productos)