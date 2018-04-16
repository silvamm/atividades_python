cont = 0
num = int(input('Digite um número: '))
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[31m', end='')
        cont += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end='\033[m ')
print('\nO número {} foi divisivel {} vezes '. format(num, cont),end='')
if cont == 2:
    print('e por isso é PRIMO!')
else:
    print('e por isso ele NÃO É PRIMO!')


