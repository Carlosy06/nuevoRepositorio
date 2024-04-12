# El usuario introduce una frase.
# El programa muestra la versión de esa frase invertida.
# utilice una función que se ejecuta una sola vez.

def frase_invertida():
    frase = input("Escribe una frase que te guste: ")
    frase_inversa = frase[::-1]
    print ("La frase que escribiste, en su versión invertida es: ", frase_inversa)
frase_invertida()
