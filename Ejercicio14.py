# Este programa solicita al usuario que escriba un valor entero.
# Posteriormente muestra si el número es par o impar.


num=int(input("Escribe un número entero: "))
if num % 2 == 0:
    print ("El número que escribiste es par.")
else:
    print ("El número que escribiste es impar.")