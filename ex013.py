print('>Aumento salarial<')
n = input('Digite o nome completo do funcionário: ')
s = (float(input('Digite o salário atual de {}: R$'.format(n))))
print('O salário de {} com o ajuste de 15% é: {:.2f}'.format(n, s+s*0.15))
