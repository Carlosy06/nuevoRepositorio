# Este programa crea un diccionario de traducción español/inglés.
# El usuario introduce las palabras en español e inglés separadas por dos puntos.
# Y cada par <palabra>:<traducción> separados por comas. Luego, se pide una frase.
# En español y se utiliza el diccionario para traducirla palabra a palabra.

# Crea un diccionario vacío para almacenar las traducciones
diccionario_traduccion = {}

entrada_usuario = input("Introduce las palabras en español e inglés (separadas por dos puntos): ")

# Divide la entrada en pares de palabras
pares_palabras = entrada_usuario.split(',')

# Crea el diccionario con las palabras y sus traducciones
for par in pares_palabras:
    palabra_espanol, palabra_ingles = par.split(':')
    diccionario_traduccion[palabra_espanol.strip()] = palabra_ingles.strip()

# Solicita la palabra en español al usuario
frase_espanol = input("Introduce la palabra en español: ")

# Traduce la frase palabra a palabra utilizando el diccionario
palabras_frase = frase_espanol.split()
frase_traducida = []
for palabra in palabras_frase:
    if palabra in diccionario_traduccion:
        frase_traducida.append(diccionario_traduccion[palabra])
    else:
        frase_traducida.append(palabra)

frase_traducida_final = ' '.join(frase_traducida)
print(f"Frase traducida: {frase_traducida_final}")
