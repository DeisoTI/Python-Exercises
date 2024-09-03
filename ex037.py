print('\033[1;30;42mConversor de bases numéricas\033[m')
número = int(input('\033[37mDigite um número inteiro: \033[m'))
print('''\033[37mEscolha uma das bases para conversão:\033[m 
\033[1;32m[ 1 ] Converter para BINÁRIO\033[m
\033[1;31m[ 2 ] Converter para OCTAL\033[m
\033[1;33m[ 3 ] Converter para HEXADECIMAL\033[m''')
opção = int(input(': '))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual a: {}'.format(número, bin(número)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(número, oct(número)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(número, hex(número)[2:]))
else:
    print('Opção inválida.')
