num = int(input('Digite um número: '))
result= num % 2 # A porcentagem serve para pegar o resto da divisão de um número
if result == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é impar.'.format(num))
