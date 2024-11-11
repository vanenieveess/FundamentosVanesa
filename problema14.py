#Ingresar 10 valores numéricos por teclado y calcular la suma,
# el promedio e imprimir la suma, el promedio agregando una leyenda en cada caso.

contador = 0
sumatoria = 0

while contador <10:
    valor = int(input('Ingresar un valor: '))
    sumatoria += valor
    contador += 1

print("La suma total es:", sumatoria)
contador = 0
suma = 0

cantidad = int(input("Ingresar los valores deseados: "))

while contador < cantidad:
    valor = float(input(f"Ingresa el valor {contador + 1}: "))
    suma += valor
    contador += 1

promedio = suma / cantidad

print(f"\nLa suma de los valores ingresados es: {suma}")
print(f"El promedio de los valores ingresados es: {promedio}")