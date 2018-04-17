#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n1 = int(input('Digite um número: '))
if n1 % n1 == 0 and n1 % 2 != 0 or n1 == 2:
    print('Esse número é primo!')
else:
    print('Esse número não é primo!')
