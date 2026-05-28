cantidad = 3
contador = 0
suma = 0

while contador < cantidad:
    numero = int(input("Ingrese un número entero: "))
    suma = suma + numero
    contador = contador + 1

media = suma / cantidad

print("La media de los números ingresados es:", media)