#ejercicio 4

energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 
intentos = 0
nombre = input("ingrese su nombre: ")
while nombre.isdigit():
    print("ingrese un nombre valido")
    nombre = input("ingrese su nombre: ")


while energia > 0 and tiempo > 0:
    print("1) forzar cerradura ")
    print("2) hackear panel ")
    print("3) descansar ")

    opcion = input("que opcion elije?: ")

    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("ingrese un numero valido")
        opcion = input("que opcion elije?: ")

    if opcion == "1":
        print("has forzado una cerradura")
        energia -= 20
        tiempo -=2
        intentos += 1

        if intentos == 3:
            print("la alarma se ah activado, la puerta esta bloqueada!!!")
            print("DERROTA")
            break
    
        else:
            if energia < 40:

                numero = input("que numero elije?(1-3): ")

                while not numero.isdigit():
                    print("ingrese un numero valido")
                    numero = input("que numero elije?: ")

                if numero == "3":
                    alarma = True
                    print("la alarma se ah activado, la puerta esta bloqueada!!!")
                else:
                    cerraduras_abiertas += 1
                    print("has abierto una cerradura")
            else:
                cerraduras_abiertas += 1
                print("has abierto una cerradura")

    elif opcion == "2" :
        intentos = 0
        energia -= 10
        tiempo -= 3
        for i in range(4):
            print(f"hackeando.... paso{i + 1}")
            codigo_parcial += "A"


        print(f"codigo parcial:{codigo_parcial}")

        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            print("cerradura abierta por hackeo")

    elif opcion == "3" :
        intentos = 0
        if energia >= 100:
            print("el limite de cura es de 100")
            continue
        if energia < 100:
            print("estas descansando!!")
            energia += 15
            tiempo -= 1

    if cerraduras_abiertas == 3:
        print("VICTORIA")
        break

    if energia <= 0 or tiempo <= 0 or alarma == True:
        print("DERROTA")
        break