contraseña = input("ingrese su contraseña: ")
longitud = len(contraseña) 

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")