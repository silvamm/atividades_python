#Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 


homens = mulheresmenores = maiores = 0
while True:
    print('='*40)
    print('CADASTRE UMA PESSOA'.center(40))
    print('='*40)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower().strip()[0]
    while sexo not in 'mf':
            sexo = str(input('Opção inválida! Sexo [M/F]: ')).lower().strip()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'm':
        homens += 1
    if idade < 20 and sexo == 'f':
        mulheresmenores += 1
    resposta = str(input('Você deseja continuar? [S/N] ')).lower().strip()[0]
    while resposta not in 'sn':
            resposta = str(input('Opção inválida! Você deseja continuar? [S/N]')).lower().strip()[0]
    if resposta == 'n':
        break
print('====== FIM DO PROGRAMA ======')
print(f'O número de pessoas maiores de 18 anos é {maiores}\nO número de homens cadastrados é {homens}\nO número de mulheres menores de 20 anos é {mulheresmenores}')





