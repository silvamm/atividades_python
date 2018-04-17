#Escreva um programa que faça o computador "pensar" em um número inteiro 
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

#OBS: Esse programa foi melhorado no exercicio '058'.

from random import randint #import random 1ª Tentativa
from time import sleep
x = 'Jogo da Advinhação v1.0'
print('-=-'*20)
print(x.center(60))
print('-=-'*20)
                  #l = [1, 2, 3, 4, 5] 1ª Tentativa
nr = randint(0,5) #nr = random.choice(l) 1ª Tentativa
n = int(input('O computador escolherá um número de 0 a 5 aleatoriamente, tente advinha-lo!\nDigite um número: '))
print('PROCESSANDO ... ')
sleep(2)
if nr == n:
    print('O computador escolheu {}. Parabéns, você acertou!'.format(nr))
else:
     print ('O computador escolheu {}. Que pena, você errou!'.format(nr))






