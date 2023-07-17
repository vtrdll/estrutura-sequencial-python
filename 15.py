#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


# 1 litro para 6 metros

# 18 litros pinta  108 metros R$ 80 REAIS 
#3.6 litros pinta  21.6 metros R$ 25 REAIS 

metros=float(input("Digite a quantidade em metros quadrados a ser pintado: "))#200

tinta= metros / 6 #200/6 = 33.33333

print("Voce ira precisar de ",tinta,"litros de tinta ")
print()
#comprar apenas latas de 18 litros
print("Para comprar apenas latas de 18 litros voce vai preecisar de: ")
latas = tinta //18 
print("Voce ira precisar de: %.i latas de tinta" %latas)
print("O valor fica de: R$ %.2f reais " %(latas*80))



#comprar apenas galoes de 3.6 litros
print()
print("Para comprar apenas galoes de 3.6 litros: ")
latas2 = tinta //3.6
print("Voce vai precisar de: %.i galoes de tinta "%latas2)
print("O valor fica de: R$ %.2f reais " %(latas2*25))
print()
#miisutar galoes e latas

folga = tinta * 1.1
litros = folga // 18

folga_faltando= folga -(latas*18)
galoes=  (folga_faltando // 3.6 )

custo = (litros*80)+(galoes*25.)
print("Mix de latas e galoes: ")
print("Cliente precisa comprar" ,litros, "latas e ",galoes, "que custaram R$ %i" %custo)

    


        
