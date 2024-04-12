# Este programa solicita la edad del usuario.
# Devuelve los años que has cumplido, reflejandolo en pantalla.

edad = int(input("Ingresa tu edad en números enteros: "))
for i in range(edad):
    print("Usted ha cumplido " + str(i + 1) + " años")
