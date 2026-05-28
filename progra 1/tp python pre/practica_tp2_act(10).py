hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día: "))

if hemisferio == "N":
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Invierno"

elif hemisferio == "S":
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Verano"
else:
    estacion = "Hemisferio inválido"

print("La estación es:", estacion)
