from random import randint
a = int(input('Tente adivinhar o número que estou pensando: '))
pc = randint(0,5)
while a != pc:
    print('Número errado')
    a = int(input('Tente novamente: '))
print('Você acertou!')
