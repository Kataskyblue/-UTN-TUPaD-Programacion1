magnitud = float(input("ingrese la magnitud: "))

if magnitud < 3:
     print("muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
     print("leve (ligeramente perceptible)")
elif magnitud >= 5 and magnitud < 6:
     print("fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
     print("muy fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 7:
     print("extremo (puede causar graves daños a gran escala)")    
