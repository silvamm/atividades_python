import random
a1 = input('Qual o 1º nome? ')
a2 = input('Qual o 2º nome? ')
a3 = input('Qual o 3º nome? ')
a4 = input('Qual o 4º nome? ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será' ,lista,)
