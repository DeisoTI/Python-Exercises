p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = p1 + (10 - 1) * r
for pa in range (p1, decimo , r):
    print(pa, end=(' '))
