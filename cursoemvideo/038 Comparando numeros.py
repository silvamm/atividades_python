#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais


programa = 'Vamos comparar dois números ...'
print(programa)
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
if n1>n2:
    print('O 1º número é de maior valor.')
elif n2>n1:
    print('O 2º número é de maior valor.')
elif n1==n2:
    print('Os dois números tem o mesmo valor.')




