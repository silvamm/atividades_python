d = float(input('Quantos km tem a viagem que você quer fazer ? '))
if d<=200:
    print('A passagem para esta viagem custará R${:.2f}'.format(d*0.5))
else:
    print('A passagem para esta viagem custará R${:.2f}'.format(d*0.45))
    # p = d*0.5 if d<=200 else d*45