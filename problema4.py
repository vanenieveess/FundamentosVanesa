# Calcular la nota del trimestre a partir de tres notas, luego determinar si aprobó o
# debe recuperar e informarlo.

nota1 = int(input("Ingresar nota1"))
nota2 = int(input("ingresar nota2"))
nota3 = int(input("ingresar nota3"))

promedio = ( nota1 + nota2 + nota3) / 3
if promedio >= 70:
    print ("aprobó")
elif promedio <70.:
    print ("no aprobó")




