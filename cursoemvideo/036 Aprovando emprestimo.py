#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

programa ='Minha casa, minha vida! v1.0'
print('='*60)
print(programa.center(60))
print('='*60)
valorc = float(input('Qual o valor da casa que deseja comprar? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Em quantos anos você quer liquidar? '))
prestacao = valorc / (anos * 12)
limite = salario * 30 / 100
if prestacao <= limite:
    print('Seu emprestimo bancário foi aprovado e sua casa própria é uma realidade!\n'
          'Você vai pagar R${:.2f} por mês durante {} anos.\n'
          'Parabéns!'.format(prestacao, anos))
else:
    print('Infelizmente seu empréstimo bancário não pôde ser aprovado.\n'
          'O valor da prestação ficaria por R${:.2f}, o que ultrapassa 30% o seu salário, que seria R${:.2f}.\n'
          'Por favor, refaça os cálculos aumentando o número de anos a pagar.'.format(prestacao, limite))




