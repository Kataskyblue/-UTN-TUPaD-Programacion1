#actividad 7

asistencias = [
    "Michel",
    "Jerelmy",
    "Michel",
    "Arata",
    "Jerelmy",
    "Michel"
]

print("lista original")
print(asistencias)

empleados = set(asistencias)

print("asistieron al menos una vez")
print(empleados)

contador = {}

for nombre in asistencias:

    if nombre in contador:
        contador[nombre] += 1
    else:
        contador[nombre] = 1

print("cantidad de asistencias:")

for nombre, cantidad in contador.items():
    print(nombre, "asistio", cantidad, "veces")