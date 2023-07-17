#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.



metros=int(input("Digite a area em metros quadrados a ser pintada: "))
resto = metros % 3
resto *= 0.5
litros = (metros //3) + resto


if litros<18:
   litros_resto = litros - 18
   print("Voce ira precisar de 1 Lata de tinta: ")
   print("O valor sera: R$ 80.00 ")
else:
    latas = (litros//18) 
    preco = latas*80
    print("Voce ira precisa de: %i Latas de tinta"%latas)
    print("O total fica de: R$ ",preco,"reais")

