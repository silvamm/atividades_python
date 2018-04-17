#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

import math
x = float(input('Qual o valor do cateto oposto? '))
y = float(input('Qual o valor do cateto adjacente? '))
z = math.sqrt(x ** 2 + y ** 2)
print('O valor da hipotenusa é {}.'.format(z))

