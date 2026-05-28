#actividad 1

edad = int(input("introduzca su edad: "))
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")

#actividad 2

nota = int(input("ingrese su nota: "))
if nota >= 6:
    print("esta aprobado")
else:
    print("esta deaprobado")

#actividad 3

numero_par = int(input("ingrese un numero: "))

if numero_par % 2 == 0:
    print("ingreso un numero par: ")
else:
    print("porfavor ingrese un numero par!: ")

#actividad 4

edad = int(input("ingrese su edad: "))

if edad < 12:
    print("es un niño")
elif edad >= 12 and edad <18:
    print("es un adolecente")
elif edad <= 18 and edad >30:
    print("es un adulto joven")
elif edad < 30:
    print("es un adulto")    

#actividad 5

contraseña = input("ingrese su contraseña: ")
longitud = len(contraseña) 
if longitud < 8 and longitud > 14:
    print( "Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#actividad 6

import statistics

numeros = [1, 6, 6, 7, 8, 9]

media = statistics.mean(numeros)
mediana = statistics.median(numeros)
moda = statistics.mode(numeros)

if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo (asimetría a la derecha)"
elif media < mediana and mediana < moda:
        sesgo = "Sesgo negativo (asimetría a la izquierda)"
else:
        sesgo = "No hay sesgo significativo (distribución simétrica)"

print(f"Lista: {numeros}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Resultado: {sesgo}")

#actividad 7

entrada = input("Ingresa una frase o palabra: ")

if entrada[-1].lower() in 'aeiouáéíóú':
    entrada += "!"    
print(entrada)

#actividad 8

entrada = input("ingrese su nombre: ")
numero = int(input("un numero del 1 al 3: "))

if numero == 1:
     print(entrada.upper())
elif numero == 2:
     print (entrada.lower())
elif numero == 3:
     print(entrada.capitalize())

#actividad 9

magnitud = float(input("ingrese la magnitud: "))

if magnitud < 3:
     print("muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
     print("leve (ligeramente perceptible)")
elif magnitud >= 5 and magnitud < 6:
     print("fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
     print("muy fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 7:
     print("extremo (puede causar graves daños a gran escala)")    

#actividad 10  

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día: "))

if hemisferio == "N":
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Invierno"

elif hemisferio == "S":
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Verano"
else:
    estacion = "Hemisferio inválido"

print("La estación es:", estacion)