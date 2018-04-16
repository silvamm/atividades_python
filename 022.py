n = str(input('Escreva seu nome: ')).strip()
print('Analisando seu nome ...')
print('Seu nome em maiúsculas é {}.'.format(n.upper()))
print('Seu nome em minúsculas é {}.'.format(n.lower()))
print('Seu nome inteiro tem {} letras.'.format (len(n) - n.count(' ')))
s = n.split()
print('Seu primeiro nome é {} e tem {} letras.' .format(s[0], len(s[0])))













