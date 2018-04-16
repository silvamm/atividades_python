s = float(input('Por favor, informe seu salário para que possamos calcular seu aumento: R$'))
if s>1250:
    print('Seu salário terá um aumento de 10% e passará para {}.'.format((s*10/100)+s))
if s<=1250:
    print('Seu salário terá um aumento de 15% e passará para {}.'.format((s*15/100)+s))


