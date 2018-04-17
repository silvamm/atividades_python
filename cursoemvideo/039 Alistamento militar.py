#Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
prog = '\033[1;32mAlistamento militar. Chegou a hora ?\033[m'
print('\033[32m~\033[m'*40)
print(prog.center(50))
print('\033[32m~\033[m'*40)
print()
nome = str(input('Qual o seu nome? ')).title()
ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
alistamento = atual - ano

if alistamento == 18:
    print('É a hora certa para se alistar, {}! Procure a junta de serviço militar mais próxima.'.format(nome))
elif alistamento < 18:
    print('Ainda não é a hora para se alistar, {}. Faltam {} anos até lá. Fique atento!'.format(nome, (18-alistamento)))
elif alistamento > 18:
    print('Já se passaram {} anos do prazo de alistamento, {}. Regularize sua situação!'.format((alistamento - 18), nome))