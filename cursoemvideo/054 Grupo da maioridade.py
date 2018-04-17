#Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maiores = 0
menores = 0
anoatual = date.today().year
for c in range (1, 8):
    ano = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if anoatual - ano < 21:
        menores = menores + 1
    elif anoatual - ano >= 21:
        maiores = maiores + 1
print('O número de pessoas maiores de idade é {} e o de menores é {}.'.format(maiores, menores))
