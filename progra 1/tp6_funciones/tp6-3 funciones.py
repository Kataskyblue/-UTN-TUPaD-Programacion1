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