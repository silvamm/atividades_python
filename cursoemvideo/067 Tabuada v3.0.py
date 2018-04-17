#Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo. 

c = 1
prog = 'TABUADA v3.0'
print('='*40)
print(f'Bem vindo ao {prog}!'.center(40))
print('='*40)
n = int(input('TABUADA do número: '))
if n >= 0:
    while True:
        print(f'{n} X {c:2} = {n * c}')
        c += 1
        if c == 11:
            n = int(input('TABUADA do número: '))
            if n >= 0:
                c = 1
            else:
                break
print(f'Fim do programa {prog}')











