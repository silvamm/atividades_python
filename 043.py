prog = 'Calculando seu IMC'
print()
print(prog)
print()
peso = float(input('Qual é seu peso?(KG) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura **2)

if imc < 18.5:
    print('Seu IMC é {:.1f}. Você está ABAIXO do peso ideal.'.format(imc))
elif imc == 18.5 or imc <= 25:
    print('Seu IMC é {:.1f}. Você está com o PESO IDEAL.'.format(imc))
elif imc == 25 or imc <= 30:
    print('Seu IMC é {:.1f}. Você está com SOBREPESO.'.format(imc))
elif imc == 30 or imc <= 40:
    print('Seu IMC é {:.1f}. Você está OBESO.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f}. Você está com OBESIDADE MÓRBIDA.'.format(imc))


