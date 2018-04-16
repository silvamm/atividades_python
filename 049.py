n = int(input('Você quer saber a tabuada do número ... ? '))
print('A tabuada do número {} é:'.format(n))
for c in range (1,11,):
    print('{} x {:2} é {}.'.format(n, c, c*n))