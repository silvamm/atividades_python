v = int(input('Qual a velocidade do carro em Km/h? '))
if v<=80:
    print('Você está dentro da velocidade permitida.')
else:
    print('Você utrapassou o limite de velocidade.\nSua multa será de R${:.2f}!.'.format((v - 80)*7))