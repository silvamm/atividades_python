#Faça um programa que leia o nome completo de uma pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual seu nome completo ? ')).split()
print('Seu primero nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))


