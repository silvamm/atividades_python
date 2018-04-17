#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
a1 = input('Qual o 1º nome? ')
a2 = input('Qual o 2º nome? ')
a3 = input('Qual o 3º nome? ')
a4 = input('Qual o 4º nome? ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será' ,lista,)
