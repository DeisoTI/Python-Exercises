print('-=-'*9)
print('Analisador de triângulos')
print('-=-'*9)
a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))
# Triângulo
if a < a + b and b < c + a and c < b + c:
    print('Os segmentos podem formar um triângulo.')
    if a == b and b == c:
        print('Esse triângulo é equilatero.')
    elif a == b and a != c or a == c and a != b or c == b and c != a:
        print('Esse triângulo é isósceles')
    else:
        print('Esse triângulo é escaleno')
# Não triângulo
else:
    print('Os segmentos não podem formar um triângulo.')
