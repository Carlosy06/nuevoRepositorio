# ingrese su nombre completo y el programa muestra en pantalla el nombre completo 3 veces.
# Muestra una versión del nombre solo con letras minúsculas.
# Muestra una versión del nombre solo con letras mayúsculas.
# Muestra una versión del nombre solo con la primera letra del nombre y de los apellidos en mayúsculas.

nombre_completo = input ("Ingresa tu nombre completo: ")

#Para nombre en minúsculas.
nombre_minusculas = nombre_completo.lower()
print (nombre_minusculas)

#Para nombre en mayúsculas.
nombre_mayusculas = nombre_completo.upper()
print (nombre_mayusculas)

#Para primera letra en mayúscula.
nombre_pletra = nombre_completo.title()
print (nombre_pletra)