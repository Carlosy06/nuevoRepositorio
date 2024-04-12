# Este programa solicita escribir un número entero positivo.
# Muestra una cuenta regresiva desde el número que el usuario escribio.

numero=int(input("Escribe un número entero positivo: "))
for i in range(numero, -1, -1):
    print (i, end= ",")