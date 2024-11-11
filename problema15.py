# Ingresar 100 valores por teclado y determinar cuántas veces el valor ingresado
#es: a) Mayor a 0 y menor a 10
#Esta comprendido entre 10 y 100 ambos inclusive.
# Es mayor a 100
# Es negativo
# Es igual a Olmprimir los resultados.

mayor_a_cero_y_menor_a_100 = 0
entre_10_y_100 = 0
mayor_a_100 = 0
negativo = 0
igual_a_cero = 0
contador = 0

while contador < 100:
    valor = float(input("Ingresa un valor: "))

    if 0 < valor < 100:
        mayor_a_cero_y_menor_a_100 += 1
    if 10 <= valor <= 100:
        entre_10_y_100 += 1
    if valor > 100:
        mayor_a_100 += 1
    if valor < 0:
        negativo += 1
    if valor == 0:
        igual_a_cero += 1
    contador += 1

print(f"\nMayor a cero y menor a 100: {mayor_a_cero_y_menor_a_100} veces")
print(f"Comprendido entre 10 y 100 (inclusive): {entre_10_y_100} veces")
print(f"Mayor a 100: {mayor_a_100} veces")
print(f"Negativo: {negativo} veces")
print(f"Igual a cero: {igual_a_cero} veces")