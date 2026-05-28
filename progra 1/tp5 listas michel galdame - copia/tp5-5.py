# ejercicio 5
alumnos = ["jose", "martin", "antonito", "marcos", "ricardo fort", "mateo", "milo", "juan"]

opcion = input("desea agregar o quitar un estudiante?[quitar/agregar]: ").lower()
if opcion == "agregar":
    agregar = input("a que alumno desea agregar?: ").lower()
    alumnos.append(agregar)
elif opcion == "quitar":
    quitar = input("que alumno desea quitar?: ").lower()
    alumnos.remove(quitar)
else:
    print("ingrese una opcion valida")

print("lista de alumnos: ", alumnos)
    
