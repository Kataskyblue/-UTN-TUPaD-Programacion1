herramientas =  ["pera"]
existencias = [2]


while True:
    print("menu de herramientas")
    print("1) carga inicial")
    print("2) carga existencias")
    print("3) ver inventario")
    print("4) consulta de stock")
    print("5) reporte de agotados")
    print("6) alta de nuevo producto")
    print("7) actualizacion de stock (venta/ingreso)")
    print("8) salir")

    opcion = input("ingrese una opcion (1/8):").strip().lower()

    while not opcion.isdigit():
        print("ingrese un numero adecuado")
        opcion = input("ingrese una opcion (1/8):").strip().lower()
    opcion = int(opcion)

    if opcion == 1:
        cantidad = input("cantidad de herramientas que desea agregar: ").strip().lower()
        while not cantidad.isdigit():
            print("ingrese un numero adecuado")
            cantidad = input("cantidad de herramientas que desea agregar:").strip().lower()
        cantidad = int(cantidad)        
        for i in range(cantidad):
            herramienta = input(f"herramienta {i+1}: ").strip().lower()
            while herramienta == "" or herramienta in herramientas:
                if herramienta == "":
                    print("espacio vacio")
                else:
                    print("herramienta duplicada")
                herramienta = input(f"herramienta {i+1}: ").strip().lower()
            herramientas.append(herramienta)

    elif opcion == 2:
        if len(herramientas) == 0:
            print("sin existencias")
        else:
            for i in range(len(herramientas)):
                print(f"herramienta : {herramientas[i]}")
                existencia = input("ingrese existencias: ").strip().lower()
                while not existencia.isdigit():
                    print("ingrese un numero valido")
                    existencia = input("ingrese existencias: ").strip().lower()
                existencias.append(int(existencia))
    elif opcion == 3:
        if herramientas == 0:
            print("no hay heramientas cargadas")
        else:
            for i in range(len(herramientas)):
                print(f"herramietas {herramientas[i]} existencias {existencias[i]}")

    elif opcion == 4:
        print("buscar herramienta")
        buscar = input("que herramienta busca?: ")
        if buscar in herramientas:
            indice = herramientas.index(buscar)
            print(f"herramienta {herramientas[indice]} cantidad: {existencias[indice]}")
        else:
            print("la herramienta no esta en la lista ")
    elif opcion == 5:
        print("lista de agotados")
        if len(herramientas) == 0:
            print("no hay agotados")
        else:
            for i in range(len(herramientas)):
                if existencias[i] == 0:
                    print(f"{herramienta[i]}: agotado")
    elif opcion == 6:
        print("alta nuevo producto")
        nuevo_producto = input("ingrese la nueva herramienta: ")
        while not nuevo_producto.isalpha():
            print("opcion invalida")
            nuevo_producto = input("ingrese la nueva herramienta: ")
        nuevo_producto = input(nuevo_producto)

        if nuevo_producto == "":
            print("espacio vacio ingrese de nuevo")
        else:
            print("herramienta duplicada")
        herramientas.append(input(nuevo_producto))
        existencias.append(int(1))
    elif opcion == 7:
        ingresar = input("ingrese la herramienta: ").strip().lower()
        while not ingresar.isalpha():
            print("opcion invalida")
            ingresar = input("ingrese la herramienta: ").strip().lower()

        ingresar = input(ingresar)
        i = herramientas.index(buscar)
        print(f"{buscar} tiene {existencias[i]} unidades")
        elegir = input("que desea hacer?(venta/ingreso):").strip().lower()

        while elegir == "":
            print("espacio vacio")
            elegir = input("que desea hacer?(venta/ingreso):").strip().lower()
        elegir = input(elegir)

        if  elegir == "venta":
            vender =  input("que cantidad desea vender?: ").strip().lower()
            while not vender.isdigit():
                print("ingrese un numero valido")
                vender = input("cuantas unidades vendio?: ").strip().lower()
            vender = int(vender)
            if vender > existencias[i]:
                print ("stock insuficiente")
            else:
                existencias[i] -= vender
                print(f"venta realizada. stock actual {existencias[i]}")
        elif elegir == "ingreso":
            cantidad = ("que cantidad desea ingresar?: ").strip().lower()
            while not cantidad.isdigit():
                print("ingrese un numero valido")
                cantidad = ("que cantidad desea ingresar?: ").strip().lower()
            cantidad = int(cantidad)
            existencias[i] += cantidad
            print(f"ingreso realizado, stock actual: {existencias[i]}")
            
  
    elif opcion == 8:
        print("saliedo . . .")
        break