# En un curso de computación, que consta de 24 alumnos, deberán armar un
# algoritmo que informe por pantalla el apellido
# y nombre junto a la nota de examen de cada alumno.

alumnos =[]
contador = 1

while contador <= 24:
    apellido = input("Ingresar el apellido del alumno (a):")
    nombre = input("Ingrese el nombre del alumno (a):")
    nota = float(input("Ingrese la nota del examen:"))
    print(f"Alumno: {apellido} {nombre} - Nota: {nota}")
    contador += 1

