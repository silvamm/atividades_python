#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo 
# de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('FORMANDO TRIÂNGULOS v2.0 por M&Ms')
r1 = float(input('Vamos descobrir se as três retas podem formar um triângulo !\nInforme o comprimento da 1ª reta : '))
r2 = float(input('Informe o comprimento da 2ª reta: '))
r3 = float(input('Informe o comprimento da 3ª reta: '))
print('Analisando valores ... ')
if r2-r3<r1<r2+r3 and r1-r3<r2<r1+r3 and r1-r2<r3<r2+r3:
    print('Essas medidas podem formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 !=r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Essas medidas NÃO PODEM FORMAR um triângulo.')
