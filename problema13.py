#Ingresar 10 valores por teclado y obtener la sumatoria de los mismos.
# Imprimir los resultados.

contador = 0
sumatoria = 0

while contador < 10:
    valor = float(input("Ingresa un valor: "))
    sumatoria += valor
    contador += 1

print("La suma total es:", sumatoria)