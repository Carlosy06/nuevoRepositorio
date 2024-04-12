# Este programa solicita el nombre del usuario.
# Solicita que indique si es hombre (m) o mujer (f).
# Usando la condicioanl if/else el programa decide a que grupo pertenece el usuario.

nombre = input("Escribe tu nombre: ")
genero = input("Escribe tu género (m/f): ").lower()

if genero == "m" and nombre.lower() < "n":
    print("Formas parte del grupo A.")
else:
    print("Formas parte del grupo B.")
