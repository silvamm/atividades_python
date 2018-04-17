#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


x = float(input("Qual o valor do produto ? R$ "))
d = x - (x * 5 / 100)
print('O novo valor do produto com o desconto de 5% é {:.2f}'.format(d))


