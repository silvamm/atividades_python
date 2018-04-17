#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Escolha um número '))
x = n * 2
y = n * 3
z = n **(1/2)
print('O dobro dele é {}\nSeu triplo é {}\nSua raiz quadrada é {:.2f}.'.format(x, y, z))
#print('O dobro dele é {}\nSeu triplo é {}\nSua raiz quadrada é {:.2f}.'.format ((x*2), (x*3), pow(x, 1/2)))