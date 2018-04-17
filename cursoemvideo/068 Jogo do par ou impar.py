#Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 


from random import randint
vitorias = 0
prog = 'PAR OU ÍMPAR v3.0'
print('='*40)
print(f'Bem vindo ao {prog}'.center(40))
print('='*40)
while True:
    poi = str(input('PAR ou ÍMPAR? [P/I] ')).lower().strip()[0]
    while poi not in 'pi':
            poi = str(input('Opção inválida! PAR ou ÍMPAR? [P/I] ')).lower().strip()[0]
    jogador = int(input('Escolha um número: '))
    computador = randint(0, 10)
    if (computador + jogador) % 2 != 0:
        print(f'\nVocê jogou {jogador} e o computador jogou {computador}. A soma foi {jogador + computador}, {jogador + computador} É ÍMPAR!')
        resultado = 'i'
    else:
        print(f'\nVocê jogou {jogador} e o computador jogou {computador}. A soma foi {jogador + computador}, {jogador + computador} É PAR!')
        resultado = 'p'
    if poi == resultado:
        print('Você GANHOU!\nVamos jogar novamente ...\n')
        vitorias += 1
    else:
        print(f'\nVocê PERDEU! Você venceu {vitorias} vezes.')
        break


















    #if poi != 'P' or poi != 'I':
        #poi = str(input('Opção inválida! PAR ou ÍMPAR? [P/I] ')).strip().upper()

    #if jogador + computador % 2 != 0:
        #print(f'Você jogou {jogador} e o computador jogou {computador}. O soma foi de {jogador + computador}, {jogador + computador} É ÍMPAR!')


