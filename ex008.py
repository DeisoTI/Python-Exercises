print('\033[1;30;42m-=-\033[m'*5, '\033[1;30;42mConversor de metros\033[m','\033[1;30;42m-=-\033[m'*5)
m = float(input('\033[33mDigite a quantidade de metros: \033[m'))
print('\033[1;32m{}M em centímetros[cm]= {}\033[m'. format(m, m*100))
print('\033[1;32m{}M em milímetros[mm]= {}\033[m'.format(m, m*1000))
