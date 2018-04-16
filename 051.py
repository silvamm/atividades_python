prog = '10 TERMOS DE UMA PA'
print('='*30)
print(prog.center(30))
print('='*30)
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão desta PA: '))
an = a1 + ((10 - 1) * r)
for x in range(a1, an + 1, r):
    print(x ,end=' ')






