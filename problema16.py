# Ingresar 10 valores numéricos y obtener el promedio de los que estén comprendidos
# entre 5 y 2500 ambos inclusive, imprimir el resultado.

suma = 0
contador = 0
valores_ingresados = 0

while valores_ingresados < 10:
    valor = float(input("Ingresa un valor: "))

    if 5 <= valor <= 2500:
        suma += valor
        contador += 1
    valores_ingresados += 1

if contador > 0:
    promedio = suma / contador
    print("El promedio de los valores entre 5 y 2500 es:", promedio)
else:
    print("No se ingresaron valores dentro del rango de 5 a 2500.")