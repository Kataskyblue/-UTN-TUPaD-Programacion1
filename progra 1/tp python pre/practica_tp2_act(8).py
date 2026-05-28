entrada = input("ingrese su nombre: ")
numero = int(input("un numero del 1 al 3: "))

if numero == 1:
     print(entrada.upper())
elif numero == 2:
     print (entrada.lower())
elif numero == 3:
     print(entrada.capitalize())