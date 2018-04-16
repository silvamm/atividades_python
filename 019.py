import random
a1 = input('Qual o nome do 1º aluno(a)? ')
a2 = input('Qual o nome do 2º aluno(a)? ')
a3 = input('Qual o nome do 3º aluno(a)? ')
a4 = input('Qual o nome do 4º aluno(a)? ')
r = random.choice([a1, a2, a3, a4])
print('O aluno(a) escolhido(a) foi {}'.format(r))

