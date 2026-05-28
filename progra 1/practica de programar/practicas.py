dinero_en_cuenta = 10000

dinero_a_retirar = float(int(input("ingrese la cantidad de dinero que desea retirar: ")))
if dinero_en_cuenta >= dinero_a_retirar:
    dinero_en_cuenta = dinero_en_cuenta - dinero_a_retirar
    print("retiro realizado con exito")
else:
    print(float,"saldo insuficiente. su saldo es de ${dinero_en_cuenta}")

#practica 2

edad = int(input("por favor, ingrese su edad"))

if 65 >= edad and edad < 18:
    print("debes votar obligatoriamente")
elif 18 > edad and edad >=  16 or edad >= 65:
    print("puedes votar, pero no es obligatorio")
