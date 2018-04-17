#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

a = int(input('Digite um ano: '))
b = a % 4
if b == 0 and a % 100 != 0 or a % 400 == 0:
    print('{} é  um ano Bissexto!'.format(a))
else:
    print('{} não é um ano Bissexto!'.format(a))