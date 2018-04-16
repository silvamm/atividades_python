prog ='Multifunções'
sair = 5
resposta = 0
soma = 0
multiplicar = 0
maior = 0
novos = 4
valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
while resposta != sair:
    print('Digite:\n[1] para SOMA\n[2] para MULTIPLICAR\n[3] para mostrar o MAIOR valor\n[4] para NOVOS NÚMEROS\n[5] para SAIR DO PROGRAMA.')
    resposta = int(input('Escolha uma opção: '))
    if resposta == 1:
        soma = valor1 + valor2
        print('A SOMA dos valores apresentados é {}'.format(soma))
    if resposta == 2:
        multiplicar = valor1 * valor2
        print('A MULTIPLICAÇÃO dos valores apresentados é {}'.format(multiplicar))
    if resposta == 3:
        if valor1 > valor2:
             maior = valor1
        if valor2 > valor1:
            maior = valor2
        print('O MAIOR valor apresentado é {}'.format(maior))
    if resposta == 4:
        valor1 = int(input('Digite o 1º NOVO valor: '))
        valor2 = int(input('Digite o 2º NOVO valor: '))
print('Obrigado por usar nosso programa!')


