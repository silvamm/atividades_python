#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, 
#só que agora utilizando um laço for.

#OBS: Esse programa foi melhorado no exercício '067'


n = int(input('Você quer saber a tabuada do número ... ? '))
print('A tabuada do número {} é:'.format(n))
for c in range (1,11,):
    print('{} x {:2} é {}.'.format(n, c, c*n))