s = c = 0
while True:
    n = int(input('Digite um número: [999 para PARAR] '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A quantidade de números digitados foi {c} e a soma deles é {s}')

