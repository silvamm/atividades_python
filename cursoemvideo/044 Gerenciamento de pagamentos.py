#Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros


print('{:=^40}'.format(' LOJAS MONTEIRO '))
preco = float(input('Preço das compras: R$'))
print('='*32)
print('FORMAS DE PAGAMENTO')
print('='*32)
print('''DIGITE 1 / À VISTA 
DIGITE 2 / À VISTA NO CARTÃO
DIGITE 3 / 2X NO CARTÃO
DIGITE 4 / 3X OU MAIS NO CARTÃO''')
print('='*32)
forma = int(input('Qual a forma de pagamento? '))
if forma == 1:
    print('À VISTA com 10% de desconto o produto sai por R${:.2f}!'.format(preco - (preco*10/100)))
elif forma == 2:
    print('CARTÃO 1X com 5% de desconto o produto sai por R${:.2f}.'.format(preco - (preco*5/100)))
elif forma == 3:
    print('CARTÃO 2X o preço não sofre mudança e continua por R${:.2f}, em duas de {}.'.format(preco, preco / 2))
elif forma == 4:
    parcelas = int(input('Em quantas parcelas? '))
    print('CARTÃO {}x o preço tem um acréscimo de 20% e sai por R${:.2F}, em parcelas de {}.'.format(parcelas, preco + (preco*20/100),(preco + (preco*20/100))/ parcelas ))
else:
    print('O modo de pagamento não foi digitado corretamente.')

