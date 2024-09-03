print('\033[1;30;45mPrestação de Empréstimo NUBANK\033[m')
print('\033[37m*Requisíto: A prestação mensal NÃO deve exceder 30% do salário do comprador; caso contrário, será negado.*\033[m')
casa = (float(input('\033[35mValor da Casa: R$\033[m')))
salário = (float(input('\033[35mSalário do Comprador: R$\033[m')))
anos = (int(input('\033[35mAnos para Financiamento: \033[m')))
prestação = salário*0.3 #valor do salário multiplicado por 30 por cento
if prestação * anos >= casa: # prestação multiplicado pela quantidade de anos para pagar, igual ao valor da casa
    print('\033[1;32mEmpréstimo Aprovado\033[m')
else:
    print('\033[1;31mEmpréstimo Negado\033[m')
