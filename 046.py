import emoji
from time import sleep
prog = 'Contagem Regressiva.'
start = input('Aperte ENTER para começar a contagem regressiva!')
for c in range (10, -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize(' :fireworks:'*5 + ' FELIZ ANO NOVO!' + ' :fireworks:'*5))



