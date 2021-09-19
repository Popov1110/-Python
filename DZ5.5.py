chisla = open('dz5_5.txt', 'w+')
chisla.write(input('Введите числа через пробел: '))
chisla.seek(0)
my_list = chisla.readline().split(' ')
my_intlist = [int(el) for el in my_list]
print (sum(my_intlist))
chisla.close()