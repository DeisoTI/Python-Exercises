print('\033[1;30;44m=\033[m'*10, '\033[1;30;44mTabuada digital\033[m', '\033[1;30;44m=\033[m'*10)
x = int(input('\033[1;34mDigite o número: \033[m'))
print('\033[34;40mTabuada de {}\033[m'.format(x))
for c in range (0, 10):
    print('\033[1;32m{} x {} = {}\033[m'.format(x, c, x*c))
