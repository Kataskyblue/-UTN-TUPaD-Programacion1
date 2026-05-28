herramientas = []
stock = []



while True:
    print("==menu de herramientas==")
    print("1) carga inicial de herramientas")
    print("2) carga de existencias")
    print("3) visualizacion de inventario")
    print("4) buscar herramienta")

    opcion = input("que opcion desea?")

    while not opcion.isdigit():
        print("ingrese una opcion valida")
        opcion = input("que opcion desea?")
    opcion = int(opcion)

    if opcion == 1:
        print("carga de herramientas ")
        for i in range(3):
            herramienta = input(f"ingrese herramientas{i+1}: ").strip().lower()
                
            while herramienta == "" or herramienta in herramientas:
                if herramienta == "":
                    print("nombre vacio")
                else:
                    print("herramienta duplicada")

                herramienta = input(f"ingrese herramienta {i+1}: ").strip().lower()

            herramientas.append(herramienta)
    elif opcion == 2:
        print("carga de stock")
        stock = []
        for i in range(len(herramientas)):
            print(f"herramienta : {herramientas[i]}")
            cantidad = input ("ingrese stock: ")

            while not cantidad.isdigit():
                print("ingrese un numero valido")
                cantidad = input("ingrese stock: ")
            stock.append(int(cantidad))

    elif opcion == 3:
        print("stock de las herramientas")
        print("\nInventario:")
        for i in range(len(herramientas)):
            print(f"{herramientas[i]}: {stock[i]} unidades")
            

    elif opcion == 4:
        print("buscar herramienta")
        buscar = input("que herramienta esta buscando?: ").strip().lower()
        if len(herramientas) == 0:
            print("no hay herramientas cargadas")
            continue
        elif buscar in herramientas:
            i = herramientas.index(buscar)
            print(f"{buscar}: {stock[i]} unidades disponibles")   
        else:
            print("herramienta no encontrada")


