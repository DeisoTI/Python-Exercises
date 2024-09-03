salário = float(input('Digite o seu salário atual: '))
if salário > 1250:
    aumento = (salário + (salário*0.1))
    print('Você recebeu um aumento de 10%, seu novo salário é: R${:.2f}'.format(aumento))
else:
    aumento = (salário + (salário*0.15))
    print('Você recebeu um aumento de 15%, seu novo salário é: R${:.2f}'.format(aumento))
