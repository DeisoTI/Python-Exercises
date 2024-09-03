soma = 0
for p in range (6):
    n= int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
print('a soma dos número é: {}'.format(soma))
