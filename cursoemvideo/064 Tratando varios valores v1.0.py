#Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


n = soma = c = 0
while n != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        soma += 0
    else:
        soma += n
        c += 1
print('Você digitou {} e a soma entre eles foi de {}.'.format(c, soma))


