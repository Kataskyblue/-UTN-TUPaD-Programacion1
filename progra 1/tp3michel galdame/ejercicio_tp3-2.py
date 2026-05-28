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

