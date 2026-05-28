# actividad 5
def  segundos_a_horas(segundos):
    return segundos / 3600

segundos = input("ingrese los segundos: ")
while not segundos.isdigit():
    print("ingrese un numero valido")
    segundos = input("ingrese los segundos: ")
segundos = int(segundos)


print(f"horas: {segundos_a_horas(segundos):.2f}")
