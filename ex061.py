pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da p.a: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(pt), end='')
    pt += r
    cont += 1
