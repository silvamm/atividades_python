prog = 'Calculando o fatorial'
fatorial = 0
num = int(input('Digite um número para descobrir seu fatorial: '))
if num == 1:
    fatorial = 1
while num != 1:
    if fatorial > num:
        parcial = fatorial * (num - 1)
        fatorial = parcial
        num -= 1
    if fatorial == 0:
        parcial = num * (num - 1)
        fatorial = parcial
        num -= 1
print('O fatorial é {}.'.format(fatorial))












