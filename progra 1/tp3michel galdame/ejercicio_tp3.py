#tp integrador ejercicio 1


nombre_cliente = input("ingrese su nombre porfavor: ")
while not nombre_cliente.isalpha():
    print("ingrese un nombre valido")
    nombre_cliente = input("ingrese su nombre: ")

cantidad_productos = input(" que cantidad de productos desea comprar: ")
while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("ingrese un nombre valido")
    cantidad_productos= input("que cantidad de productos desea comprar: ")
cantidad_productos = int(cantidad_productos)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(cantidad_productos):
    print(f"\nproducto {i + 1}")
    precio = input("ingrese el precio: ")
    while not precio.isdigit():
        print("ingrese un numero valido")
        precio = input("ingrese el precio: ")
    precio = int(precio)
    
    while precio <= 0:
        print("ingrese un precio superior a 0 ")
        precio = int(input("ingrese el precio: "))

    total_sin_descuento += precio

    descuento = input("tiene algun descuento? S/N: ").lower()

    while descuento != "s" and descuento != "n":
        print("ingrese S o N!!")
        descuento = input("tiene descuento? (S/N): ").lower()

    if descuento == "s":
        precio_final = precio - (precio * 0.10)
        print(f" su precio seria de {precio_final}")
        total_con_descuento += precio_final
    else:
        print(f"su precio seria de {precio}")
        total_con_descuento += precio
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos
print("\n=========================================")
print(f"cliente {nombre_cliente}")
print (f"cantidad de productos: {cantidad_productos}")
print(f"total sin descuentos ${total_sin_descuento}")
print(f"total con descuentos ${total_con_descuento}")
print(f"ahorro: {ahorro}")
print(f"promedio del producto: ${promedio:.2f}")


# ejecicio 2

usuario_correcto = "alumno"
clave_correcta = "python123"
maximos_intentos = 3

print("=|= ACCESO AL CAMPUS =|=")




while maximos_intentos > 0:
    usuario = input("ingrese su usuario: ").lower()
    clave = input("ingrese su clave: ").lower()


    if usuario != usuario_correcto or clave != clave_correcta:
        maximos_intentos -= 1
        print("usuario o clave incorrecta, intente de nuevo")

        if maximos_intentos <= 0:
            print("intentos disponibles agotados")
            print("cuenta bloqueada")
            break

    if usuario == usuario_correcto and clave == clave_correcta:
        while True:

            print("\n◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆")
            print("1) ver estado de inscripcion")
            print("2) cambiar clave")
            print("3) mostrar mensaje motivacional")
            print("4) salir")
            print("\n◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆")

            opcion = input("\nque opcion desea elegir?: ")


            while not opcion.isdigit()or int(opcion) < 1 or int(opcion) > 4:
                print("\ningrese un numero valido (1-4)")
                opcion = input("\nque opcion desea elegir?: ")

            
            if opcion == "1":
                print("inscripto")

            elif opcion == "2":
                print("cambiar clave")
                
                nueva_clave = input("ingrese la nueva clave: ")
                while len(nueva_clave) < 6 :
                    print("error: minimo 6 caracteres")
                    nueva_clave = input("ingrese la nueva clave: ")
                confirmar_clave = input("confirme la nueva clave")



                if  nueva_clave == confirmar_clave:
                    print(f"clave cambiada")
                    clave_correcta = nueva_clave
                else:
                    print("las claves no coinciden")
            
            elif opcion == "3":
                print("llegaras muy lejos en la vida")
            
            elif opcion == "4":
                print("saliendo . . .")
                break


#ejercicio 3
lunes = 4
martes = 3

#turnos

lunes_1 = ""
lunes_2 = ""
lunes_3 = ""
lunes_4 = ""

martes_1 = ""
martes_2 = ""
martes_3 = ""

operador = input("ingrese su nombre (operador): ")
while not operador.isalpha():
    print("ingrese un nombre valido")
    operador = input("ingrese su nombre (operador): ")

print(f"\nbienvenido {operador}!")

while True:


    print("\n: : : : : : : : : : : : : : : : ")
    print ("opcion 1: reservar turno")
    print ("opcion 2: cancelar turno")
    print ("opcion 3: ver agenda del dia")
    print("opcion 4: ver resumen general")
    print ("opcion 5: cerrar sistema")
    print(": : : : : : : : : : : : : : : : ")
    

    print("\n=========================================")
    opcion = input("ingrese la opcion: ")
    print("=========================================")

    if opcion.isdigit():
        opcion = int(opcion)
    else:
        print("\nerror: ingrese un numero")
        continue

    if opcion == 1:
        print("\n- - - - - - - - - - - - - -")
        print("has reservado un turno")
        print("- - - - - - - - - - - - - -")
        nombre_paciente = input("ingrese su nombre para agendar el turno: ")
        if not nombre_paciente.isalpha():
             print("ingrese un nombre valido")
             continue
        dia = input(f"\n Sr/Srta.{nombre_paciente} que dia desea reservar?(Martes o Lunes?):").title()
        if dia == "Martes":
                print("\nagendo para el dia Martes ")
                if nombre_paciente == martes_1 or nombre_paciente == martes_2 or nombre_paciente == martes_3:
                    print("ese paciente ya tiene turno en martes!")
                else:
                    if martes_1 == "":
                        martes -= 1
                        martes_1 = nombre_paciente
                        print (f"turno reservado para {nombre_paciente} para el turno 1")
                    elif martes_2 == "":
                        martes -= 1
                        martes_2 = nombre_paciente
                        print (f"turno reservado para {nombre_paciente} para el turno 2")
                    elif martes_3 == "":
                        martes -= 1
                        martes_3 = nombre_paciente
                        print (f"turno reservado para {nombre_paciente} para el turno 3")
                    else:
                        print("no hay cupos: libres!!")

        elif dia == "Lunes":
                print("\nagendo para el dia Lunes ")
                if nombre_paciente == lunes_1 or nombre_paciente == lunes_2 or nombre_paciente == lunes_3 or nombre_paciente == lunes_4:
                    print("ese paciente ya tiene turno en Lunes!")
                else:
                    if lunes_1 == "":
                        lunes -= 1
                        lunes_1 = nombre_paciente
                        print (f"turno reservado para {nombre_paciente} para el turno 1")
                    elif lunes_2 == "":
                        lunes_2 = nombre_paciente
                        lunes -= 1
                        print (f"turno reservado para {nombre_paciente} para el turno 2")

                    elif lunes_3 == "":
                        lunes_3 = nombre_paciente
                        lunes -= 1
                        print (f"turno reservado para {nombre_paciente} para el turno 3")
                    elif lunes_4 == "":
                        lunes -= 1
                        lunes_4 = nombre_paciente
                        print (f"turno reservado para {nombre_paciente} para el turno 4")
                    else:
                        print("no hay cupos: libres!!")
        else:
             print("\nopcion invalida")

    elif opcion == 2:
        nombre_paciente = input("ingrese su nombre para cancelar el turno: ")
        if not nombre_paciente.isalpha():
            print("ingrese un nombre valido")


        dia_cancelado = input(f"\n Sr/Srta.{nombre_paciente} que dia desea cancelar(Martes o lunes)?").title()
        if dia_cancelado == "Martes":
            if not dia_cancelado.isalpha():
                print("ingrese un dia valido")
                continue

        if dia_cancelado == "Lunes":
            if nombre_paciente == lunes_1:
                lunes_1 = ""
                lunes += 1
                print(f"turno de {nombre_paciente} cancelado")
            elif nombre_paciente == lunes_2:
                lunes_2 = ""
                lunes += 1
                print(f"turno de {nombre_paciente} cancelado")
            elif nombre_paciente == lunes_3:
                lunes_3 = ""
                lunes += 1
                print(f"turno de {nombre_paciente} cancelado")
            elif nombre_paciente == lunes_4:
                lunes_4 = ""
                lunes += 1
                print(f"turno de {nombre_paciente} cancelado")
            else:
                print(f"no se encontró turno para {nombre_paciente}")



        elif dia_cancelado == "Martes":
            if nombre_paciente == martes_1:
                martes_1 = ""
                martes += 1
                print(f"turno de {nombre_paciente} cancelado")
            elif nombre_paciente == martes_2:
                martes_2 = ""
                martes += 1
                print(f"turno de {nombre_paciente} cancelado")
            elif nombre_paciente == martes_3:
                martes_3 = ""
                martes += 1
                print(f"turno de {nombre_paciente} cancelado")
            else:
                print(f"no se encontró turno para {nombre_paciente}")

        

    elif opcion == 3: 
        print ("||aqui la agenda||")
        print("◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆")
        print ("turnos del Lunes ")
        if lunes_1 == "":
            print("turno numero 1°: libre")
        else:
            print ("turno numero 1°:", lunes_1)
 
        if lunes_2 == "":
            print("turno numero 2°: libre")
        else:
            print ("turno numero 2°:", lunes_2)

        if lunes_3 == "":
            print("turno numero 3°: libre")
        else:
            print("turno numero 3°:", lunes_3)
    
        if lunes_4 == "":
            print("turno numero 4°: libre")
        else:
            print ("turno numero 4°:", lunes_4)
        print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("turnos del Martes")
        if martes_1 == "":
            print ("turno numero 1°: libre")
        else:
            print("turno numero 1°:", martes_1)

        if martes_2 == "":
            print("turno numero 2°: libre" )
        else:
            print("turno numero 2°", martes_2)

        if martes_3 == "":
            print("turno numero 3°: libre" )
        else:
            print("turno numero 3°", martes_3)
        

        print ("◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆")

    elif opcion == 4:
        print("\nagenda del dia")
        print("|°|turnos del dia|°|")

        ocupados_lunes = 4 - lunes
        ocupados_martes = 3 - martes

        print(f"lunes ocupados:{ocupados_lunes} | disponibles: {lunes}")
        print(f"martes ocupados:{ocupados_martes} | disponibles: {martes}")
        
        if ocupados_lunes > ocupados_martes:
            print ("lunes tiene mas turnos ocupados")
        elif ocupados_martes > ocupados_lunes:
            print ("martes tiene mas turnos ocupados")
        elif ocupados_lunes == ocupados_martes:
            print("empate")


        

    elif opcion == 5:
        print("saliendo....")
        break

    else:
        print("\ningrese una opcion valida (1-5)")


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