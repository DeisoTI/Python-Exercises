nascimento = int(input("Digite seu ano de nascimento: "))
diferenca = 2023 - nascimento
print('Você tem {} anos'.format(diferenca))
if diferenca == 18:
    print("O seu alistamento é esse ano.")
elif diferenca > 18:
    print("Você já deveria ter se alistado há {} anos".format(diferenca - 18))
else:
    print("Você ainda tem {} faltam {} para seu alistamento será em {}".format(diferenca, 18 - diferenca, nascimento + 18))
