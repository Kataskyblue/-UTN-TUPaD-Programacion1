#ejercicio 3
import random


numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))


    pares = []
    impares = []
    for numero in numeros:
        if numero %2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

print(f"los numeros pares son { len(pares)}")
print(f"los numeros impares son {len(impares)}")