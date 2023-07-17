#Faça um Programa que peça a temperatura em graus Fahrenheit,
#transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9)


fahrenheit=int(input("Digite a temperatura em graus Fahrenheit: "))
c= 5*((fahrenheit-32)/9)
print("Temperatura em Celsius: %.2f"%c)
