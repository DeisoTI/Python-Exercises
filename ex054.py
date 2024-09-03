for a in range(1, 8):
    b = int(input('Digite o ano de nascimento da pessoa {}: '.format(a)))
    c = 2023 - b
    if c >= 18:
        print('A pessoa {} já é de maior'.format(a))
    else:
        print('A pessoa {} ainda é de menor'.format(a))
