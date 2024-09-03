print('\033[1;30;47m-=-\033[m'*5)
print(' '*3,'\033[1;31mMedidor\033[m')
print('\033[1;30;47m-=-\033[m'*5)
l = float(input('\033[37mLargura da parede: \033[m'))
h = float(input('\033[37mAltura da parede: \033[m'))
a = h*l
print('\033[1;31mNecessários: {} litros de tinta\033[m'.format(a/2))
