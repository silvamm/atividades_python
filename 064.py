n = soma = c = 0
while n != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        soma += 0
    else:
        soma += n
        c += 1
print('Você digitou {} e a soma entre eles foi de {}.'.format(c, soma))


