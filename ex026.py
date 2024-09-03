fr = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(fr.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(fr.find('A')+1))
print('A última letra "A" apareceu na posição {}'.format(fr.rfind('A')+1))
