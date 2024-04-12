# Este programa solicita al usuario una fecha en formato dd/mm/aaaa,
# la convierte en otro formato y muestra el resultado.

from datetime import datetime

fecha_string = input("Introduce la fecha en formato dd/mm/aaaa: ")

# Convertimos la cadena de texto a un objeto datetime
fecha = datetime.strptime(fecha_string, '%d/%m/%Y')

# Obtenemos el nombre del mes en español
meses = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
    5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
    9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
}

print(f"{fecha.day} de {meses[fecha.month]} del {fecha.year}")
