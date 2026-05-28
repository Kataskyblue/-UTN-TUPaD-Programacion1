CORTE = "*"
edad_minima = float("inf")
NOMBRE_INVALIDO = "XXXXXXXXXXX"
nombre_mas_joven = NOMBRE_INVALIDO

nombre = input("ingrese un nombre (" + CORTE + " para cortar) ")
while nombre != CORTE:
    edad = int(input("ingrese la edad de " + nombre + ": "))
    if edad < edad_minima:
        edad_minima = edad
        nombre_mas_joven = nombre
    nombre = input("ingrese otro nombre(" + CORTE + " para cortar): ") 

if nombre_mas_joven == NOMBRE_INVALIDO:
    print("no se ingresaron personas")
else:
    print("la persona mas joven(",edad_minima," años) es",nombre_mas_joven)