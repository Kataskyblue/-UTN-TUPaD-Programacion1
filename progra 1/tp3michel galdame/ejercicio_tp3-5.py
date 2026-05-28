#ejercicio 5

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_base_pesado = 15
daño_base_enemigo = 12
turno_de_gladiador = True


nombre = input ("nombre del gladiador :")
while not nombre.isalpha():
    print("Error : Solo se permiten letras")
    nombre = input("nombre del gladiador :")

while vida_gladiador > 0 and vida_enemigo > 0 :
    print(f"tu vida {vida_gladiador}")
    print(f"vida del enemigo {vida_enemigo}")
    print(f"pociones: {pociones}")
    print("\n°|TURNO DEL JUGADOR|°")
    print("1) ataque pesado")
    print("2) rafaga veloz")
    print("3) curar")
    opcion =input("tu turno ¿que haras?")
    while not opcion.isdigit():
        print("ingrese una opcion valida")
        opcion =input("tu turno ¿que haras?")

    if opcion == "1":
        print("\nataque pesado:")

        if vida_enemigo > 20:
            print("ataque pesado!!!")
            vida_enemigo -= daño_base_pesado
            print(f" daño de {daño_base_pesado}")
        elif vida_enemigo < 20:
            golpe_critico = daño_base_pesado *1.5
            print("golpe critico !!!")
            vida_enemigo = vida_enemigo - golpe_critico
            print(f"daño de {golpe_critico}")
    elif opcion == "2":
        print("Rafaga Veloz")
        for i in range(3):
            print (f"golpe N°{i + 1} conectado por 5 de daño")
            vida_enemigo -= 15
    elif opcion == "3":
        if pociones > 0:
            print("te has curado ")
            pociones -= 1
            vida_gladiador += 30
            if vida_gladiador > 100: 
                vida_gladiador = 100
        else:
            print("no quedan pociones!!!")
    else:
        print("ingrese una opcion valida (1-4)")
    print(f"ataque del enemigo| daño {daño_base_enemigo}")
    vida_gladiador -= daño_base_enemigo
if vida_gladiador > 0:
    print(f"victoria {nombre} ha ganado la batalla")
else:
    print("derrota, has caido en combate")