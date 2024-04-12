# Este código recoge seis números de la lotería que el usuario escribe.
# Y el programa los ordena de menor a mayor para luego imprimirlos en pantalla.

numeros_ganadores = []

for i in range(6):
    numero = int(input("Escribe un número ganador de la lotería: "))
    numeros_ganadores.append(numero)

numeros_ganadores.sort()

print("Los números ganadores ordenados de menor a mayor son:")
for numero in numeros_ganadores:
    print(numero, end=", ")
