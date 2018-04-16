sexo = 0
while sexo != 'm' and sexo != 'f':
    sexo = str(input('SEXO [M/F]: ')).lower().strip()
    if sexo != 'm' and sexo != 'f':
        print('Digite apenas F para feminino e M para masculino. Tente novamente.')
print('FIM')





