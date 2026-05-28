
entrada = input("Ingresa una frase o palabra: ")

if entrada[-1].lower() in 'aeiouáéíóú':
    entrada += "!"    
print(entrada)
