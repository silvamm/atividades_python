#Crie um programa que leia quanto dinheiro um pessoa tem na carteira 
# e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$3,27
#dolarhoje.com


r = float(input('Quantos R$ você tem ? '))
d = r / 3.27
print('Você pode comprar US$ {:.2f}.'.format(d))
