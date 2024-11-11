# Dados 3 números determinar el mayor e informar por pantalla el resultado

num1 = int(input("Ingrese mum1"))
num2 = int(input("Ingrese mum2"))
num3 = int(input("Ingrese mum3"))

if num1 > num2 and num1 > num3:
    print ("num1 es mayor")
if num2 > num1 and num2 > num3:
    print ("num2 es mayor")
if num3 > num1 and num3 > num2:
    print ("num3 es mayor")