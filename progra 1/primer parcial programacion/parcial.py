herramientas = []
existencias = []

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

    opcion = input("que opcion elige?(1-7): ")

    while not opcion.isdigit() or int(opcion) <1 or int(opcion) > 8:
        print("opcion invalida")
        opcion = input("que opcion elige?:")
    opcion = int(opcion)


    if opcion == 1:
        cantidad = input("cuantas herramientas desea cargar?: ")
        while not cantidad.isdigit() or int(cantidad) <= 0:
            print("ingrese un numero valido")
            cantidad = input("cuantas herramientas desea cargar?: ")
        cantidad = int(cantidad)
        
        for i in range(cantidad):
            herramienta = input(f"ingrese herramienta {i+1}: ").strip()
            while herramienta == "" or herramienta in herramientas:
                if herramienta == "":
                    print("nombre vacio, ingrese de nuevo")
                else:
                    print("herramienta duplicada")
                    herramienta = input(f"ingrese herramienta {i+1}: ").strip()
                herramienta = input(herramienta)
            
            herramientas.append(herramienta)

    if opcion == 2:
        if len(herramientas) == 0:
            print("no hay herramientas cargadas")
        else:
            for i in range(len(herramientas)):
                print(f"herramienta: {herramientas[i]}")
                existencia = input("ingrese existencias: ")

                while not existencia.isdigit():
                    print("ingrese un numero valido")
                    existencia = input("ingrese existencias: ")
                    
                existencias.append(int(existencia))
    if opcion == 3:
        if len(herramientas) == 0:
            print("no hay herramientas cargadas")
        else:
            for i in range(len(herramientas)):
                print(f"{herramientas[i]}: {existencias[i]} unidades")


    if opcion == 4:
        buscar = input("ingrese nombre de herramienta: ").strip().lower()
        if buscar in herramientas:
            i = herramientas.index(buscar)
            print(f"{buscar} tiene {existencias[i]} unidades")
        else:
            print("herramienta no encontrada")

    if opcion == 5:
        if len(herramientas) == 0:
            print("no hay agotados")
        else:
          for i in range(len(herramientas)):
            if existencias[i] == 0:
                print(f"{herramientas[i]} está agotado")

    if opcion == 6:
        nuevo_producto = input("ingrese el nuevo producto").strip()
        if nuevo_producto == "":
            print("nombre vacio")
            continue
        if nuevo_producto in herramientas:
            print("este producto ya se encuentra en la lista")
            continue
        stock = input("ingrese stock inicial: ")
        if not stock.isdigit() or int(stock) < 0:
            print("stock invalido")
            continue
        herramientas.append(nuevo_producto)
        existencias.append(int(stock))
        print("herramienta agregada")

    if opcion == 7:
        buscar = input("ingrese nombre de herramienta: ").strip().lower()
        if buscar in herramientas:
            i = herramientas.index(buscar)
            print(f"{buscar} tiene {existencias[i]} unidades")
            elegir = input("que desea hacer?(venta/ingreso):").lower()

            if elegir == "venta":
                cantidad = input ("cuantas unidades vendio?: ")
                
                while not cantidad.isdigit():
                    print("ingrese un numero valido")
                    cantidad = input("cuantas unidades vendio?: ")
                cantidad = int(cantidad)
                if cantidad > existencias[i]:
                    print("stock insuficiente")    
                else:
                    existencias[i] -= cantidad
                    print(f"venta realizada, stock actual: {existencias[i]}")
                    
            elif elegir == "ingreso":
                cantidad = input("cuantas unidades ingresa?: ")
                while not cantidad.isdigit():
                    print("ingrese un numero valido")
                    cantidad = input("cuantas unidades ingresa?: ")
                existencias[i] += int(cantidad)
                print(f"ingreso realizado, stock actual: {existencias[i]}")

    if opcion == 8:
        print("saliendo del sistema")
        break  

