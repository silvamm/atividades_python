prog = 'JOKENPÔ v1.0'
from random import randint
PEDRA = 1
PAPEL = 2
TESOURA = 3
computador = randint(1,3)
print()
print(prog.center(20))
print('='*20)
print('PEDRA = 1\n     PAPEL = 2\n        TESOURA = 3')
print('='*20)
jogador = input('ESCOLHA: ')
print(jogador)
if computador == jogador:
    print('EMPATE! O computador escolheu {} também!'.format(computador))
elif computador == 1 and jogador == 2:
    print('GANHOU! O computador escolheu {}!'.format(computador))
elif computador == 1 and jogador == 3:
    print('PERDEU! O computador escolheu {}!'.format(computador))
elif computador == 2 and jogador == 1:
    print('PERDEU! O computador escolheu {}!'.format(computador))
elif computador == 2 and jogador == 3:
    print('GANHOU! O computador escolheu {}!'.format(computador))
elif computador == 3 and jogador == 1:
    print('GANHOU! O computador escolheu {}!'.format(computador))
elif computador == 3 and jogador == 2:
    print('PERDEU! O computador escolheu {}!'.format(computador))
else:
    print('Você não escolheu uma opção válida!')


