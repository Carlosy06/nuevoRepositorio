# Este programa muestra las tablas de múltiplicar del 1 al 10.
# Utilicé una serie de "____________" para dividir las tablas.

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("_________________")
