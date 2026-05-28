herramientas = ["mango", "pera", "manzana"]
existencias = [67, 99, 69]
while True:
    print("==menu de herramientas==")
    print("1) carga inicial de herramientas")
    print("2) carga de existencias")
    print("3) visualizacion de inventario")
    print("4) consulta de stock")
    print("5) reporte de agotados")
    print("6) alta de nuevo producto")
    print("7) actualizacion de stock (venta/ingreso)")
    print("8) SALIR") 

    opcion = input("ingrese una opcion(1/8): ").strip().lower()

    while not opcion.isdigit():
        print("ingrese una opcion valida")
        opcion = input("ingrese una opcion(1/8): ")
    opcion = int(opcion)
    

    if opcion == 1:
        cantidad = input("ingrese las herramientas que desea ingresar: ").strip().lower()
        while not cantidad.isdigit():
            print("ingrese un numero valido")
            cantidad = input("ingrese las herramientas que desea ingresar: ").strip().lower()
        opcion = int(opcion)

        for i in range(cantidad):
            herramienta = input(f"ingrese la herramienta numero {i+1}:").strip().lower()
            while herramienta == "" or herramienta in herramientas:
                if herramienta == "":  
                    print("cargue herramientas primero")

                elif herramienta in herramientas:
                    print("herramienta duplicada")
            herramientas.append(herramienta)
    elif opcion == 2:
        if len(herramientas) == 0:
            print("no hay herramientas cargadas")
        else:
            for i in range(len(herramientas)):
                print(f"herramienta: {herramientas[i]}")
                existencia = input ("ingrese existencias: ")
                while not existencia.isdigit():
                    print("ingrese un numero valido")
                    existencia = input ("ingrese existencias: ")
                existencias.append(int(existencia))
    elif opcion == 3:
          print("inventario")

          for i in range(len(herramientas)):
            print(f"herramienta: {herramientas[i]} unidades: {existencias[i]}")
    elif opcion == 4:
        print("buscar la herramienta")
        buscar = input("que herramienta busca?: ").strip().lower()

        while not buscar.isalpha():
            print("ingrese solo letras")
            buscar = input("que herramienta busca?: ").strip().lower()


        if buscar in herramientas:
            i = herramientas.index(buscar)
            print(f"herramienta {herramientas[i]} unidades {existencias[i]}")
        else:
            print("herramienta no encontrada")
    elif opcion == 5:
        print("lista de agotados:")
        for i in range(len(herramientas)):
            if existencias[i] == 0:
                print(f"herramientas agotadas: {herramientas[i]} ")
                hay_agotados = True
        if not hay_agotados:
            print("sin elemenos agotados")
    elif opcion == 6:
        nuevo_producto = input("ingrese un producto nuevo: ").strip().lower()
        while not nuevo_producto.isalpha():
            print("ingrese un nombre valido")
            nuevo_producto = input("ingrese un producto nuevo: ").strip().lower()
        while nuevo_producto == "" or nuevo_producto in herramientas:
            if nuevo_producto == "":
                print("no ingrese espacios vacios")
            else:
                print("el producto ya esta en la lista")
                nuevo_producto = input("ingrese un producto nuevo: ").strip().lower()

        herramientas.append(nuevo_producto)
        existencias.append(1)
    elif opcion == 7:
        print("Actualización de Stock ")
        elegir = input("(Venta/Ingreso):").strip().lower()

        while not elegir.isalpha():
            print("ingrese un nombre valido")
            elegir = input("(Venta/Ingreso): ").strip().lower()

        if elegir == "venta":
            producto = input("que producto desea vender?: ").strip().lower()

            if producto in herramientas:
                posicion = herramientas.index(producto)
                cantidad = input("cantidad a vender").strip().lower()
                while not cantidad.isdigit():
                    print("ingrese un numero valido")
                    cantidad = input("cantidad a vender: ").strip().lower()
                cantidad = int(cantidad)

                if cantidad <= existencias[posicion]:
                    existencias[posicion] -= cantidad
                else:
                    print("no hay suficiente stock")
            else:
                print("primero ingrese una herramienta")
        elif elegir == " ingreso":
            producto = input("que producto desea ingresar?: ").strip().lower()
            if producto == "":
                print("espacio en blanco")
                continue

            if producto in herramientas:
                posicion = herramientas.index(producto)
                cantidad = input(" cantidad a ingresar: ")
                while not cantidad.isdigit():
                    cantidad = input(" cantidad a ingresar: ")
                cantidad = int(cantidad)
                existencias[posicion] += cantidad
    elif opcion == 8:
        print("saliendo. . .")
        break





        
 


