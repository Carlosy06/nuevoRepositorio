# Este programa muestra el símbolo de una divisa basado en un diccionario predefinido.
# Si la divisa no está en el diccionario, se muestra un mensaje de aviso.

divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
divisa_usuario = input("Ingresa una divisa (Euro, Dollar o Yen): ")
if divisa_usuario in divisas:
    print(f"El símbolo de {divisa_usuario} es {divisas[divisa_usuario]}")
else:
    print("La divisa ingresada no está en el diccionario.")
 