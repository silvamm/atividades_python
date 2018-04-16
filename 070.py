total = maisde1000 = nomebarato = precobarato = 0
while True:
    print('='*40)
    print('MERCADINHO SÓ O BOM'.center(40))
    print('='*40)
    produto = str(input('PRODUTO: '))
    preco = float(input('PREÇO: R$'))
    total += preco
    if preco > 1000:
        maisde1000 += 1
    if nomebarato == 0 or precobarato > preco:
        nomebarato = produto
        precobarato = preco
    resposta = str(input('Deseja continuar? [S/N] ')).lower().strip()
    while resposta not in 'sn':
            resposta = str(input('Resposta inválida! Deseja continuar? [S/N] '))
    if resposta == 'n':
        break
print('========== FIM DO PROGRAMA ===========')
print(f'O total da compra foi de R${total:.2f}\nTivemos {maisde1000} produtos com preço maior que R$1000.00\nO produto mais barato foi {nomebarato} que custa {precobarato}.')





