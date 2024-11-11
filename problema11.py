# Ingresar un valor por teclado y determinar si es menor que 10 si está comprendido
#entre 10 y 100 o si es mayor a 100, imprimir una leyenda, repetir el proceso 10 veces.

contador = 0

while contador <10:
    valor = int(input("Ingresar un valor:"))

    if valor <10:
        print ("El valor es menor que 10")
    elif 10<= valor <=100:
        print ("El valor está entre 10 y 100")
    if valor >100:
        print ("El valor es mayor del rango")