# ejercicio 13

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print(f"puntaje mas alto {max(puntajes)}")
print(f"puntaje mas bajo {min(puntajes)}")
print(f"ranking {sorted(puntajes, reverse = True)}")
ranking = sorted(puntajes, reverse=True)
print(f"el numero 990 se encuentra en la posicion {ranking.index(990 )+1}")