#Faça um Programa que peça a temperatura em graus Celsius,
#transforme e mostre em graus Fahrenheit.

celsius=int(input("Digite a temperatura em Celsius: "))
f=(celsius*9)/(5) + 32
print("Temperatura em Fahrenheit: %.2f graus"%f)
