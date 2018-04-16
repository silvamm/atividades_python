n1 = float(input('Qual a 1ª nota? '))
n2 = float(input('Qual a 2ª nota? '))
media = (n1+n2)/2
if media < 5:
    print('Sua média foi {:.1f}. Você está \033[1;31mREPROVADO!\033[m'.format(media))
elif media == 5  or media <= 6.9:
    print('Sua média foi {:.1f}. Você está em \033[1;34mRECUPERAÇÃO!\033[m'.format(media))
else:
    print('Sua média foi {:.1f}. Você foi \033[1;32mAPROVADO!\033[m'.format(media))


