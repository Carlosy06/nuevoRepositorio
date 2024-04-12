# Este programa guarda una contraseña en una variable.
# El programa muestra si la contraseña introducida por el usuario es la misma que se allmacenó en la variable.

contraseña= "carlitos"
contraseña_usuario= input ("Introduce la contraseña: ")
if contraseña_usuario.lower()==contraseña.lower():
    print ("La contraseña es la misma, correcta.")
else:
    print ("La contraseña no es la misma, incorrecta.")