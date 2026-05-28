#actividad 1

def imprimir_hola_mundo():
    print("hola mundo")

imprimir_hola_mundo()

#actividad 2

nombre = input("ingrese su nombre")

def saludar_usuario(nombre):
   return (f"hola {nombre}")


print(saludar_usuario(nombre))

#actividad 3

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
while not edad.isdigit():
    print("ingrese un numero valido")
    edad = input("ingrese su edad: ")
residencia = input("ingrese su residencia (provincia): ")
def informacion_personal(nombre, apellido,edad, residencia ):

    print (F"soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

informacion_personal(nombre, apellido, edad, residencia)

#actividad 4

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2  
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio      
radio = input("ingrese el radio: ")
while not radio.isdigit():
    print("ingrese un numero valido")
    radio = input("ingrese el radio: ")
radio = int(radio)

print(f"area: {calcular_area_circulo(radio):.2f}")
print(f"perimetro: {calcular_perimetro_circulo(radio):.2f}")

