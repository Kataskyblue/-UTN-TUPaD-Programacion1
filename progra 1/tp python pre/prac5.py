import statistics

numeros = [90, 84, 6, 70, 87, 1]
media = statistics.mean(numeros)
mediana = statistics.median(numeros)
moda = statistics.mode(numeros)

if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo (asimetría a la derecha)"
elif media < mediana and mediana < moda:
        sesgo = "Sesgo negativo (asimetría a la izquierda)"
else:
        sesgo = "No hay sesgo significativo (distribución simétrica)"

print(f"Lista: {numeros}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Resultado: {sesgo}")