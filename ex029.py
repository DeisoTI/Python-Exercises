velocidade = float(input('Digite a velocidade do carro(km/h): '))
if velocidade > 80:
    print('Você excedeu o limite de velocidade permitido por lei.')
    multa = ((velocidade-80)*7)
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tudo nos conformes.')
