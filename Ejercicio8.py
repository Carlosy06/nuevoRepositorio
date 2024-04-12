# Solicita un nombre.
# Muestra la versión de dicho nombre escrito en mayúsculas.
# Muestra la cantidad de letras que componen al nombre.

nombre = input ("Escribe tu nombre: ")
nombre_mayusculas = nombre.upper ()
cantidad_letras= len (nombre)
print (f"{nombre_mayusculas} tiene {cantidad_letras} letras.")