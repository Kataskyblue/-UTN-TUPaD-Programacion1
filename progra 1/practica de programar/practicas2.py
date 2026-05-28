#practica 2

edad = int(input("por favor, ingrese su edad"))

if 65 >= edad and edad < 18:
    print("debes votar obligatoriamente")
elif 18 > edad and edad >=  16 or edad >= 65:
    print("puedes votar, pero no es obligatorio")
