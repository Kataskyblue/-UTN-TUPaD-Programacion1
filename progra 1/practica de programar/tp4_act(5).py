lista_estudiantes_presentes = ["mads mikkelsen ", "león kennedy", "henry cavill", "ash williams", "bruce campbell", "ricardo iorio", "ricardo fort", "jason voorhees"]

elegir = input("agregara o quitara un estudiante?:")
if elegir == "agregar":
    agregar = lista_estudiantes_presentes.append(input( "que estudiante desea agregar?: "))
    print(lista_estudiantes_presentes)
elif elegir == "quitar":
    quitar = lista_estudiantes_presentes.remove(input("que estudiante eliminara?: "))
    print(lista_estudiantes_presentes)

