#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo1 = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = int(input('Em uma sequência de: '))
n = 1
while c!= 0 :
    an = termo1 + (n - 1) * razao
    n += 1
    c -=1
    print(an, end=' ')