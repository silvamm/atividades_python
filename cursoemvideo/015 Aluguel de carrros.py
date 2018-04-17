#Escreva um programa que pergunte a quantidade de Km percorridos 
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


x = int(input('Quanto dias de aluguel ? ' ))
y = float(input('Quantos quilômetros rodados ? '))
pxy = (x * 60) + (y * 0.15)
print('O valor a ser pago é de R${:.2f}'.format(pxy))