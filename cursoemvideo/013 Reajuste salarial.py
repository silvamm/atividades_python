#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual é salário? R$ '))
a = s + (s * 15 / 100)
print('O salário apresentando com o aumento de 15% passa para R${}.'.format(a))
