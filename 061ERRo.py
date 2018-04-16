termo1 = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
n = 1
mais = 1
while mais != 0:
    while n <= 10:
        an = termo1 + (n - 1) * razao
        n += 1
        mais += 1
        print (an, end=' ')
    print('PAUSA')
    mais = int(input('\nVocê gostaria de ver mais quantos termos? '))
    n = mais










