x = int(input('Quanto dias de aluguel ? ' ))
y = float(input('Quantos quilômetros rodados ? '))
pxy = (x * 60) + (y * 0.15)
print('O valor a ser pago é de R${:.2f}'.format(pxy))