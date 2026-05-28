import random
numero_secreto = random.randint(0,9)
intentos = 0

while True:
    intentos = int(input("adivina el numero: "))
    intentos = intentos + 1
    if intentos == numero_secreto:
        print(f"genial, ganaste tomo {intentos} intentos")
