# Este programa hace la división de dos números enteros.
# Muestra un error en el caso de intentar hacer división entre 0.

n1= int(input("Escribe un número entero: "))
n2= int(input("Escribe otro número entero: "))
if n2==0:
    print ("Error, no puedes dividir entre 0.")
else:
    resultado= (n1/n2)
    print("El resultado de la división de ambos números es: ", resultado)
