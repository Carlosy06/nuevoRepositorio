# Solicita un número de celular con la extensión +34.
# El programa muestra en pantalla el número de celular sin el prefijo y tampoco la extensión.

celular = input ("Ingresa el número de celular en el formato +34-número-extensión: ")
partes = celular.split("-")
numero = partes [1]
print (f"El número de celular sin el prefijo y la extensión es: {numero}")