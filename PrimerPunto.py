#1. Elabore un programa en Python que permita convertir de pesos a dólares, de
#pesos a euros, de euros a pesos, de pesos a yenes. (10 ptos)
#1 yen = 26.30 pesos
#1 dólar = 3944 pesos
#1 euro = 4279 pesos
import os
yen = 26.30
dolar = 3944
euro = 4279
pesos = 4285
valor = 0
elecc = ''
pasar = ''
result = 0
print("""
            ************************ 
            * CONVERSOR DE MONEDAS *
            ************************
          """)
print ("Opciones:")
print("1. Pesos a Dolares")
print("2. Pesos a Euros")
print("3. Euros a Pesos")
print("4. Pesos a Yenes")
op = (int(input("Ingrese una Opcion: ")))
while op < 1 or op > 4:
    op = (int(input("Opcion no Valida, intentelo nuevamente: ")))

if op == 1:
    elecc = "pesos"
    pasar = "dolares"
    valor = float(input("Ingrese la cantidad de pesos: "))
    while valor < 0:
        valor = float(input("Ingrese un numero valido: "))
    result = valor * dolar
elif op == 2:
    elecc = "pesos"
    pasar = "euros"
    valor = float(input("Ingrese la cantidad de Pesos"))
    while valor < 0:
        valor = float(input("Ingrese un numero valido: "))
    result = valor * euro
elif op == 3:
    elecc = "Euros"
    pasar = "Pesos"
    valor = float(input("Ingrese la cantidad de Euros"))
    while valor < 0:
        valor = float(input("Ingrese un numero valido: "))
    result = valor * pesos
elif op == 4:
    elecc = "pesos"
    pasar = "yenes"
    valor = float(input("Ingrese la cantidad de Pesos"))
    while valor < 0:
        valor = float(input("Ingrese un numero valido: "))
    result = valor * yen

os.system("cls")
print("Resultados:")
print(f'{valor} {elecc} son {result} {pasar}')
os.system('pause')