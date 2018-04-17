#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
#e R$0,45 parta viagens mais longas.

d = float(input('Quantos km tem a viagem que você quer fazer ? '))
if d<=200:
    print('A passagem para esta viagem custará R${:.2f}'.format(d*0.5))
else:
    print('A passagem para esta viagem custará R${:.2f}'.format(d*0.45))
    # p = d*0.5 if d<=200 else d*45