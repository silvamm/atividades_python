#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
m = (n1+n2)/2
#print('A média do aluno(a) é',m,'. ')
print('A média do aluno(a) é {:.1f}.'.format (m))

