print('-=-'*4)
print('Caixa C&A')
print('-=-'*4)
print('Olá, seja bem-vindo')
produto = float(input('Digite o valor do produto: '))
pagamento = int(input('Qual a forma de pagamento? \n Cartão - 1 \n Dinheiro ou Cheque - 2 \n'))
if pagamento == 1:
    forma = int(input(' [ 1 ] à vista \n [ 2 ] 2 vezes \n [ 3 ] 3 vezes \n'))
    if forma == 1:
        print("Você recebe 5% de desconto, preço final:{}".format(produto - produto*0.05))
    elif forma == 2:
        print("Preço formal:{}".format(produto))
    elif forma == 3:
        print("O valor será acrescentado 20% de juros: {}".format(produto + produto*0.2))
    else:
       print("Código inválido")

elif pagamento == 2:
    print("Você terá um desconto de 10%, valor final {}".format(produto - produto*0.1))
