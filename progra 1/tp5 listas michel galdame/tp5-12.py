#ejercicio 12

lista = []

for i in range(1, 9):
    numeros = int(input(f"ingrese el numero {i}: "))
    lista.append(numeros)
print(f"lista: {lista}")
print(F"numeros de menor a mayor: {sorted(lista)}")
print(f"numeros de mayor a menor: {sorted(lista, reverse=True)}")