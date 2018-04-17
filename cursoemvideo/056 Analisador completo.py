# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


prog = 'Triagem Maluca.'
soma = 0
maior = 0
menor = 0
idmaior = 0
for nis in range (0, 4):
    print('------ {}ª PESSOA -------'.format(nis + 1))
    nome = str(input('NOME: ' )).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).lower().strip()
    soma += idade
    if sexo == 'f' and idade < 20:
        menor += 1
    if nis == 1 and sexo == 'm':
         maior = nome
         idmaior = idade
    if sexo == 'm' and idade > idmaior:
            idmaior = idade
            maior = nome
print()
print('A medida da idade do grupo é {} anos.'.format(soma/4))
print('O nome do homem mais velho é {} e tem {} anos.'.format(maior, idmaior))
print('{} mulheres são menores de 20 anos.'.format(menor))














