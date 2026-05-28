mi_primer_string = "mi string con comillas dobles"
mi_segundo_string = "mi segundo string"


otro_string = "hola"

a,b,c,d = otro_string

print(a)
print(b)
print(c)
print(d)
#pone todo en mayuscula
print(mi_primer_string.upper())  
#hace la primera letra en mayuscula
print(mi_primer_string.capitalize())
#pone todo en minuscula
print(mi_primer_string.lower())
#cuenta los caracteres
print(len(mi_primer_string))
#encuentra la letra que le indicamos
print(mi_primer_string.find("s"))
#cuenta la cantidad de veces que sale un caracter
print(mi_primer_string.count("a"))
#se pueden combinar, aqui pregunta al programa si
print(mi_primer_string.upper().isupper) 
 