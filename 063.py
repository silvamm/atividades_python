prog ='Sequência de Fibonacci'
print(prog)
n= int(input('Quantos termos você quer ver? '))
c = 3
num1 = 0
num2 = 1
print(num1, num2, end =' ')
while c <= n:
    num3 = num1 + num2
    print(num3, end=' ')
    c += 1
    num1 = num2
    num2 = num3


