# ejercicio 11
 
lista = ["jose", "martin", "antonito", "marcos", "ricardo fort", "mateo", "milo", "juan", "teo", "pancho"]

buscar_nombre = input("que nombre desea buscar?: ").lower()
if buscar_nombre in lista:
    print("nombre en la lista!!")
    print(f"Esta en ña posicion {lista.index(buscar_nombre) +1 }")
else:
    print("el nombre no se encuentra ")


