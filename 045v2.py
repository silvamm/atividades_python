prog = 'JOKENPÔ v1.0'
from time import sleep
from random import choice
itens = 'PEDRA PAPEL TESOURA'
opcoes = itens.split()
while True:
    computador = choice (opcoes)
    print()
    print(prog.center(20))
    print('='*24)
    print('PEDRA, PAPEL OU TESOURA?')
    print('='*24)
    jogador = input('ESCOLHA: ').upper()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print()
    if computador == jogador:
        print('EMPATE! O computador escolheu {} também!'.format(computador))
    elif computador == 'PEDRA' and jogador == 'PAPEL':
        print('GANHOU! O computador escolheu {}!'.format(computador))
    elif computador == 'PEDRA' and jogador == 'TESOURA':
        print('PERDEU! O computador escolheu {}!'.format(computador))
    elif computador == 'PAPEL' and jogador == 'PEDRA':
        print('PERDEU! O computador escolheu {}!'.format(computador))
    elif computador == 'PAPEL' and jogador == 'TESOURA':
        print('GANHOU! O computador escolheu {}!'.format(computador))
    elif computador == 'TESOURA' and jogador == 'PEDRA':
        print('GANHOU! O computador escolheu {}!'.format(computador))
    elif computador == 'TESOURA' and jogador == 'PAPEL':
        print('PERDEU! O computador escolheu {}!'.format(computador))
    else:
        print('Essa jogada não é válida!')


