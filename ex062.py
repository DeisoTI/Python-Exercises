pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da p.a: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = mais + total
    while cont <= total:
        print('{} -> '.format(pt), end='')
        pt += r
        cont += 1
    print('pausa')
    mais = int(input('Quantos anos você quer mostrar a mais? '))
print('Fim')
