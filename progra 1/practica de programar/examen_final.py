#PROYECTO FINAL
titulos = []
ejemplares = [] 
# titulos = [ "El Señor De Los Anillos", "Orgullo Y Prejuicio", "Matar Un Ruiseñor" ]
# ejemplares = [5, 7, 9]


opcion = ""
while (opcion != "7"):
    print("---------------------------")
    print("\n    BIBLIOTECA - Menu ")
    print("---------------------------")
    print("1) ingresar titulos")
    print("2) Mostrar catálogo")
    print("3) Consultar disponibilidad")
    print("4) Listar agotados ") 
    print("5) Agregar título")
    print("6) Actualizar ejemplares (préstamo/devolución)")
    print("7) Salir")

    opcion = input("elegi una opcion (1-7): ").strip()

    match opcion:
        #ingresar titulos
        case "1":
            print("ingresar titulos (carga inicial)")
            print("cuantos libros son?")
            
            cantidad_str = input().strip()
            while not cantidad_str.isdigit():
                print("ingresa un numero valido")
                cantidad_str = input("que cantidad desea agregar?: ")

            cantidad = int(cantidad_str)
            i = 0
            while i < cantidad:
                print(f"ingresando el titulo de {i+1}° libro")
                titulo = input().strip().title()

                print("cuantas copias desea ingresar?: ")
                copias = input().strip()
                while not copias.isdigit():
                    print("ingresa un numero valido")
                    copias = input("que cantidad desea agregar?: ").strip()

                # titulos.append(titulo)
                # ejemplares.append(int(copias))

                duplicado = False
                j = 0

                while not duplicado and j <len(titulos):
                    if titulos[j]== titulo:
                        duplicado = True
                        i-=1
                        print(f"el libro {titulo} ya existe en el catalogo")
                    j += 1

                if not duplicado:
                    titulos.append(titulo)
                    ejemplares.append(int(copias))
                    print(f" libro {titulo} agregado correctamente.")
                i += 1

        #mostrar catalogo
        case "2":
            print("================================")
            print("\ncatalgo de libros y stock")
            print("================================")

            if len(titulos) > 0:
                for i in range(len(titulos)):
                    print(f"{i+1} libro: {titulos[i]} ejemplares: {ejemplares[i]}")
            else:
                print("sin catalogo aun")
        #consultar disponibilidad
        case "3":
            print("consultar diponibilidad")
            titulo = input("ingrese el titulo del libro que busca: ").strip().title()
            #Buscamos el libro
            
            encontrado = False
            i = 0

            while i < len(titulos):
                if titulos[i] == titulo:
                    print(f"hay {ejemplares[i]} copias del libro {titulos[i]}")
                    encontrado = True
                i += 1
            if not encontrado:
                print("no se necontro el libro")
        
        #lista de agotados
        case "4": 
            hay_agotados = False
        
            limite = min(len(titulos), len(ejemplares))
            for i in range(limite):
                if ejemplares[i] == 0:
                    print(f"agotado: {titulos[i]}")
                    hay_agotados = True
            if not hay_agotados:
                print("no hay agotados")

        case "5":
            print("agregar titulo")
            continuar = True

            while continuar:
                titulo = input("ingrese el titulo del libro, pulse enter para salir \n").strip().title()

                if titulo == "":
                    continuar= False
    
                else:
                    duplicado = False
                    i = 0
                    
                    while not duplicado and i < len(titulos):
                        if titulos[i] == titulo:
                            duplicado = True
                            print(f"Ya ingreso el libro {titulos[i]}") 
                        i += 1 

                    if not duplicado:
                        print("cuantas copias desea ingresar?: ")
                        copias = input().strip()

                        while not copias.isdigit():
                            print("ingrese un numero positivo")
                            copias = input("cuantas copias desea ingresar?: ").strip()
                            #Agregamos el libro al catalogo
                        titulos.append(titulo)
                        ejemplares.append(int(copias))

                        print("libro agregado correctamente")
                    continuar = False

                    if not continuar:
                        print("\ncatalgo de libros y stock")
                        if len(titulos) > 0:
                            for i in range(len(titulos)):
                                print(f"{i+1} libro: {titulos[i]} ejemplares: {ejemplares[i]}")
                        else:
                            print("sin titulos aun")             
        #Actualizar ejemplares (préstamo/devolución)
        case "6":
            print("Actualizar ejemplares (préstamo/devolución)") 
            titulo = input("ingrese el titulo del libro a modificar: ").strip().title()
            #revisamos que exista
            existente = False
            i = 0
            while not existente and i < len(titulos):
                if titulos[i] == titulo:
                    existente = True
                    indice = i
                i += 1 
            #una vez que existe, procedemos a devolver / pedir prestado
            if not existente:
                print(f"El libro {titulo} no se encuentra disponible")
            else:
                print(f"{i+1} libro: {titulos[indice]} ejemplares: {ejemplares[indice]}")
                print("que desea hacer con el libro? ")
                print("1) pedir prestamo")
                print("2) devolver libro")
                modificacion = input("")
                while modificacion != "1" and modificacion != "2":
                    modificacion = input("opcion incorrecta debes ingresar 1 / 2 ")
                match modificacion:
                    #prestamo
                    case "1":

                        if ejemplares[indice] > 0:
                            ejemplares[indice] -= 1
                            print("prestamo exitoso")
                        else:
                            print(f"lo sentimos, no quedan ejemplares del libro: {titulos[indice]}")

                    #devolucion
                    case "2":
                        ejemplares[indice] += 1
                print(f"ejemplar actualizado. ahora son: {ejemplares[indice]} ejemplares en la biblioteca")                       
                  
                        
        case "_":
            print("elija del 1 al 7 porfavor")



print("saliendo. . . . .")