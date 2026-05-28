import random
numero_secreto = [random.randint(1,100) for i in range(15)]

pares = []
impares = []

for num in numero_secreto:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista de pares:", pares)
print("Lista de impares:", impares)

print("cantidad de pares: ", len(pares))
print("cantidad de pares: ", len(impares))