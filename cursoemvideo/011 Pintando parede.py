#Faça um programa que leia a largura e a altura de uma parede em metros, calcule
# a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
# litro de tinta, pinta uma área de 2m².

l = float(input('Qual a largura da parede ? '))
a = float(input('Qual a altura da parede? '))
ap = l * a
t = ap / 2
print('A area da sua parede é de {} m²'.format(ap))
print('A quantidade necessaria para pintar esta parede é {} L de tinta.' .format(t))