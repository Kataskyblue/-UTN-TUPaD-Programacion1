# ejercicio 2
lista = []

for i in range(5):
    productos = input(f"ingrese el  producto N°{i + 1}: ")
    lista.append(productos)

lista.sort()
print(lista)
