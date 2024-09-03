from random import randint
from time import sleep
print('-=-'*20)
print('Estou pensando em um número de 0 a 5, tente adivinhar')
print('-=-'*20)
pc = randint(0, 5)
resposta = int(input('Resposta: '))
print('PROCESSANDO INFORMAÇÃO...')
sleep(4)
if resposta == pc:
    print('PARABÉNS, VC É INCRIVELL!!!')
else:
    print('Vc e burro.')
