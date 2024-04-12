# Este programa crea un diccionario vacío y lo llena con información sobre una persona.
# Solicita al usuario datos como nombre, edad, sexo, teléfono y correo electrónico.
# Y muestra el contenido del diccionario cada vez que se añade un nuevo dato.

# Crea un diccionario vacío para almacenar la información de la persona.
datos_persona = {}

datos_persona['nombre'] = input("Ingresa el nombre de la persona: ")
datos_persona['edad'] = input("Ingresa la edad de la persona: ")
datos_persona['sexo'] = input("Ingresa el sexo de la persona: ")
datos_persona['teléfono'] = input("Ingresa el número de teléfono de la persona: ")
datos_persona['correo'] = input("Ingresa el correo electrónico de la persona: ")

print("Contenido del diccionario:")
for clave, valor in datos_persona.items():
    print(f"{clave}: {valor}")
