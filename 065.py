c = n = soma = media = maior = menor = resposta = 0
while resposta != 'n' :
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    resposta = str(input('Que continuar? [S/N] ')).lower().strip()[0]
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média deles é {}.'.format(c, soma/c))
print('O MAIOR número que você digitou foi {} e o MENOR foi {}.'.format(maior, menor))
