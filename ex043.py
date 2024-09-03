h = float(input("Digite sua altura: "))
p = float(input("Digite seu peso: "))

imc = p / (h*h)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está no peso ideal.")
elif imc < 30:
    print("Você está acima do peso.")
elif imc < 40:
    print("Você está obeso.")
else:
    print("Você está com obesidade mórbida")
