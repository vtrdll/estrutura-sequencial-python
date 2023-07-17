#Faça um programa que peça o tamanho de um arquivo para download (em MB)
#a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado
#de download do arquivo usando este link (em minutos).

# 1MB = 1.048.576 BYTES = 8.048.576 bits
# 250Mbps = 250.00.000 Bytes = 258.00.000 bits por segundo 
arquivo=int(input("Digite o tamanho do arquivo em MB: "))
link=int(input("A velocidade de um link de internet (em Mbps): "))
tempo=(arquivo/link)*(60)#phyton aparentemente buga quando usamos % e uma operacao matematica apos
print("Voce levara o tempo de: %.0f minutos" %tempo)


