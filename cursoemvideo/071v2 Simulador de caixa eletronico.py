#Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*40)
print('BANCO SUA DÍVIDA NOSSA ALEGRIA'.center(40))
print('='*40)
while True:
    valor = int(input('VALOR DO SAQUE: R$'))
    n50 = int(valor / 50)
    resto = valor % 50
    if valor <= 0:
        print('Esse valor não pode ser sacado.')
    if resto != valor:
        print(f'O total de cédulas de R$50 é {n50}.')
    if resto >= 20:
        n20 = int(resto / 20)
        resto = valor % 20
        print(f'O total de cédulas de R$20 é {n20}.')
    if resto >= 10:
        n10 = int(resto / 10)
        resto = valor % 10
        print(f'O total de cédulas de R$10 é {n10}.')
    if resto >= 1:
        n1 = int(resto)
        resto = valor % 1
        print(f'O total de cédulas de R$1 é {n1}')
    break
print('='*40)
print('Volte sempre!')









