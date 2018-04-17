#Faça um programa que leia um ângulo qualquer 
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
x = float(input('Digite um ângulo: '))
y = math.radians(x)
s = math.sin(y)
c = math.cos(y)
t = math.tan(y)
print('O seno desse ângulo é {}\nO cosseno desse ângulo é {} \nE a tangente é {}'.format(s, c, t))

