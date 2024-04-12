# Solicita al usuario que introduzca el número de horas trabajadas.
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))

# Solicita al usuario que introduzca el costo por hora trabajada.
coste = float(input("Introduce el costo por hora trabajada: "))

# Calcula el pago.
pago = horas_trabajadas * coste

# Muestra en pantalla el pago.
print(f"El pago para el trabajador es: {pago} Lps.")
