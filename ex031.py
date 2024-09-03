km = float(input('Digite a distância do seu destino(km/h): '))
if km > 200:
    preso = (km*0.45)
    print('Valor da passagem: R${:.2f}'.format(preso))
else:
    preso = (km*0.50)
    print('Valor da passagem: R${:.2f}'.format(preso))
