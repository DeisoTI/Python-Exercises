nas = int(input("Digite seu ano de nascimento"))
idade = 2023 - nas
print("Você tem {} anos".format(idade))
if idade <= 9:
    print("Você está na categoria mirim")
elif idade <= 14:
    print("Você está na categoria infantil")
elif idade <= 19:
    print("Você está na categoria júnior")
elif idade <= 25:
    print("Você está na categoria senior")
else:
    print("Você está na categoria master")
