#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.



hora=int(input("Digite quantas horas voce trabalha no mes: "))
ganho=float(input("Digite quanto voce ganha por hora: "))

salario_bruto = hora * ganho 
imp_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

print("Seu salario bruto: ",salario_bruto)
print("Voce pagou ao INSS: ",inss)
print("Voce pagou ao sindicato: ",sindicato)

print("+ Salário Bruto: R$ ",salario_bruto)
print("- IR (11%): R$ ",imp_renda)
print("- INSS (8%): R$ ",imp_renda)
print("- Sindicato (5%): R$ ",sindicato)
salario_bruto = salario_bruto -(inss)-(sindicato)-imp_renda
print("= Salário liquido: R$ ",salario_bruto)




