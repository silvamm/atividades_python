print('='*15,'> \033[1;31mConversão de Base\033[m <','='*15)
num = int(input('Digite um numero inteiro: '))
print('Escolha: 1 para Binario, 2 para Octal ou 3 para Hexadecimal')
op = int(input('Opção: '))
result = 0

if op == 1:
   print('Binario:',bin(num)[2:])
elif op == 2:
    print('Octal:',oct(num)[2:])
elif op == 3:
    print('Hexadecimal:',hex(num)[2:])
else:
    print('Opção Invalida!')