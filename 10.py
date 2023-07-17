#Faça um Programa que peça 2 números inteiros e um número real.
#Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.


num_int1=int(input("Digite um numero inteiro: "))
num_int2=int(input("Digite um numero inteiro: "))
num_real=float(input("Digite um numero real: "))

dobro= (2*num_int1)+(num_int2//2)
soma= (3*num_int1) + (num_real)
cubo= num_real**3
print("Dobro do primeiro com metade do segundo: ",dobro)
print("A soma do triplo do primeiro com o terceiro: ",soma)
print("O terceiro elevado ao cubo: ",cubo)
