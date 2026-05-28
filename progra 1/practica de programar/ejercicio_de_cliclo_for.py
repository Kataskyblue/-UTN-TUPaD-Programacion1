numero = int(input("ingrese un numero entre 1 y 10: "))

if numero >= 1 and numero <= 10:
    for cont in range (1,11):
        print(cont)
else:
    print("no puso un numero entre 1 y 10")

#(2)

numero = int(input("ingrese un numero entre 1 y 10: "))

if numero >= 1 and numero <= 10:
    for cont in range (1,11):
        print(numero, "x",cont,"="(numero * cont))
else:
    print("no puso un numero entre 1 y 10")
