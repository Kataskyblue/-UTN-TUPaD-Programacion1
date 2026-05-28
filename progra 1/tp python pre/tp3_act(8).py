cantidad = 3

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