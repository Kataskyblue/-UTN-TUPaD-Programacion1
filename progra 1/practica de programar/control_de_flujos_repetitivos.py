#ejercicio 1

"""imprimi los numeros del 1 al 10 pero detenelo si encontras un numero divisible por 7(usa break)"""

for numero in range (1,11):
    if numero % 7 == 0:
        break
    print(numero )

#ejercicio 2

"""imprimi los numeros del 1 al 10 pero saltea los multiplos de 3(usa continue)"""

for numero in range(1,11):
    if numero % 3 == 0:
        continue
print(numero)

#ejercicio 3

"""crea un bucle for vacio que se va a usar mas adelante(usa pass)"""

for numero in range (1,11):
    pass