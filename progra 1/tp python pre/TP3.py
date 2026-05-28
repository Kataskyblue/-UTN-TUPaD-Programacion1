#actividad 1

for i in range(1,101):
    print(i)

#actividad 2

numero = int(input("ingrese un numero: "))
cantidad = len(str(numero))
print(cantidad)

#actividad 3

inicio = int(input("ingrese el primer valor: "))
fin = int(input("ingrese el segundo valor: "))

if inicio > fin:
    inicio, fin = fin, inicio

suma =0

for i in range(inicio + 1, fin):
    suma += i

print("la suma de los numeros es: ",suma)

#actividad 4

suma = 0

while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    
    if numero == 0:
        break
    
    suma += numero

print("La suma total es:", suma)
 
#actividad 5

import random
numero_secreto = random.randint(0,9)
intentos = 0

while True:
    intentos = int(input("adivina el numero: "))
    intentos = intentos + 1
    if intentos == numero_secreto:
        print(f"genial, ganaste tomo {intentos} intentos")

#actividad 6

for i in range(100,0,-2):
    print(i)

#actividad 7

numero = int(input("numero: "))

suma = 0
cont = 0

while cont <= numero:
    suma += cont
    cont += 1

print("suma: ",suma)

#actividad 8

cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input("ingrese un numero entero: "))

if numero %2 == 0:
    pares += 1
else:
    impares += 1

if numero > 0:
    positivos += 1
elif numero < 0:
    negativos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

#actividad 9

cantidad = 3
contador = 0
suma = 0

while contador < cantidad:
    numero = int(input("Ingrese un número entero: "))
    suma = suma + numero
    contador = contador + 1

media = suma / cantidad

print("La media de los números ingresados es:", media)

#actividad 10

numero = input("Ingrese un número: ")

invertido = numero[::-1]

print("El número invertido es:", invertido)
