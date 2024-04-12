# Este programa solicita al usuario su nombre, edad, dirección y teléfono,
# y almacena esta información en un diccionario. Luego, muestra un mensaje con los detalles ingresados por el usuario.

# Creaun diccionario vacío para almacenar la información
datos_usuario = {}

datos_usuario['nombre'] = input("Ingresa tu nombre: ")
datos_usuario['edad'] = input("Ingresa tu edad: ")
datos_usuario['dirección'] = input("Ingresa tu dirección: ")
datos_usuario['teléfono'] = input("Ingresa tu número de teléfono: ")

print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['dirección']} y su número de teléfono es {datos_usuario['teléfono']}.")
