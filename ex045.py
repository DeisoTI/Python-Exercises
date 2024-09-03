from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint (0,2)
j = int(input('Escolha sua jogada: \n [ 1 ] Pedra \n [ 2 ] Papel \n [ 3 ] Tesoura \n'))
print('O computador escolheu {}'.format(itens[computador]))

if computador == 0 and j == 1: #computador jogou pedra
    print('Empate')

elif computador == 0 and j == 2:
        print('Você venceu')

elif computador == 0 and j == 3:
        print('Você perdeu')

elif computador == 1 and j == 1: #computador jogou papel
        print('Você perdeu')

elif computador == 1 and j == 2:
        print('Empate')

elif computador == 1 and j == 3:
        print('Você venceu')

elif computador == 2 and j == 1: #computador joga tesoura
        print('Você venceu')

elif computador == 2 and j == 2:
        print('Você perdeu')

elif computador == 2 and j == 3:
        print('Empate')

else:
    print("Jogada inválida.")
