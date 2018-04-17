#Faça um programa que mostre na tel
#com uma pausa de 1 segundo entre eles.
# contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, 

import emoji
from time import sleep
prog = 'Contagem Regressiva.'
start = input('Aperte ENTER para começar a contagem regressiva!')
for c in range (10, -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize(' :fireworks:'*5 + ' FELIZ ANO NOVO!' + ' :fireworks:'*5))



