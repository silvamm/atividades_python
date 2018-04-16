from datetime import date
prog = ' Sistema de categorias da Confederação Nacional de Natação Brasileira (CNNB) '
print('~'*80)
print(prog.center(80))
print('~'*80)
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
resultado = atual - ano
if resultado <= 9:
    print('Você tem {} anos e se enquadra na categoria MIRIM.'.format(resultado))
elif resultado <= 14:
    print('Você tem {} anos e se enquadra na categoria INFANTIL.'.format(resultado))
elif resultado <= 19:
    print('Você tem {} anos e se enquadra na categoria JÚNIOR.'.format(resultado))
elif resultado <= 20:
    print('Você tem {} anos e se enquadra na categoria SÊNIOR.'.format(resultado))
elif resultado >= 20:
    print('Você tem {} anos e se enquadra na categoria MASTER.'.format(resultado))