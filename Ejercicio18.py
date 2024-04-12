# Este programa solicita escribir un número entero positivo.
# Muestra todos los números impares hasta llegar al número que el usuario ingreso.

numero = int(input("Introduce un número entero positivo: "))
for i in range(1, numero + 1):
    if i % 2 != 0:
        print(i, end=", ")
