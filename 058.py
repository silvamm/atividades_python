prog = 'Jogo da advinhação v2.0'
from random import randint
jogador = 0
computador = 1
tentativas = 0
print('O computador vai escolher um número de 0 a 10, tente advinhar!.')
while jogador != computador:
    computador = str(randint(0, 10))
    jogador = input('Digite um número: ').strip()
    tentativas += 1
    if jogador == computador and tentativas == 1:
        print('PARABÉNS! Você acertou de primeira! O computador escolheu {}!'.format(computador))
    if jogador == computador and tentativas > 1:
        print('PARABÉNS! Você acertou na {}ª tentativa. O computador escolheu {} também.'.format(tentativas, computador))
    if jogador != computador:
        print('Tente novamente! O computador escolheu {}.'.format(computador))
print('FIM')


