print('\033[1;31;40mAlugômetro\033[m')
km = float(input('\033[37mQuantidade de quilômetros percorridos: \033[m'))
dias = float(input('\033[37mDias com o veículo: \033[m'))
print('\033[1;31mO cliente deve pagar: R${:.2f}\033[m'.format(dias*60+km*0.15))
