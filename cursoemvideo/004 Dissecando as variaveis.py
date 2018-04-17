#Faça um programa que leia algo pela teclado e mostre na tela o seu tipo primitivo e todas as informações
#possiveis sobre ele.

x = str(input('Digite algo: '))
print('O tipo primitivo desse valor é', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está escrito em letras maiúsculas?', x.isupper())
print('Está escrito em letras minúsuculas?', x.islower())

