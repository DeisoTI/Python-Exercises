s = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
while s != 'F' and s != 'M':
    print('Caractere inválido')
    s = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
print('Fim')
