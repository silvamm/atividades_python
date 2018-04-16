frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso =''
# inverso = junto[::-1] #podemos fazer sem o FOR
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('O inverso de {} é {}'.format(junto, inverso))
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')


