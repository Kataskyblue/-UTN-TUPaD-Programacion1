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
