#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


num = int(input('Digite um número: '))
par = num % 2
if par == 0:
    print('Esse número é PAR.')
else:
    print('Esse número é ÍMPAR.')


