# Este programa ordena una lista con las asignaturas.
# Pregunta la nota que el estudiante obtuvo en determinada clase.
# Muestra una lista con el mensaje "En "tal" asignatura usted sacó: "

asignaturas = ["Dibujo Técnico", "Educación Física", "Química", "Artística", "Taller de Agropecuaria"]
notas = {}

for asignatura in asignaturas:
    nota = input(f"¿Qué nota sacó en {asignatura}? ")
    notas[asignatura] = nota

for asignatura, nota in notas.items():
    print(f"En {asignatura} usted sacó {nota}")
