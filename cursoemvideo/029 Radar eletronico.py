#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h,mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual a velocidade do carro em Km/h? '))
if v<=80:
    print('Você está dentro da velocidade permitida.')
else:
    print('Você utrapassou o limite de velocidade.\nSua multa será de R${:.2f}!.'.format((v - 80)*7))