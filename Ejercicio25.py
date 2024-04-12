# Este programa solicita al usuario que escriba una palabra.
# La ejecución del código se encarga de contar el número de veces que se repite una vocal.

palabra = input("Escribe una palabra: ").lower()
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    count = palabra.count(vocal)
    print(f"La vocal '{vocal}' aparece {count} veces en la palabra.")
