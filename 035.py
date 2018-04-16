print('FORMANDO TRIÂNGULOS v1.0 por M&Ms')
r1 = float(input('Vamos descobrir se as três retas podem formar um triângulo!\nInforme o comprimento da 1ª reta : '))
r2 = float(input('Informe o comprimento da 2ª reta: '))
r3 = float(input('Informe o comprimento da 3ª reta: '))
print('Analisando valores ... ')
if r2-r3<r1<r2+r3 or r1-r3<r2<r1+r3 or r1-r2<r3<r2+r3:
    print('Essas medidas podem formar um triângulo! Divirta-se!.')
else:
    print('Essas medidas NÃO podem formar um triângulo! Uma pena ...')