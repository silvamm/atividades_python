#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Escreva seu nome completo: '))
print('Essa nome tem "Silva?" {}.'.format('silva' in nome.lower()))
