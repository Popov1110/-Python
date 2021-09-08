try:
    my_list = input('Введите числа через пробел: ').split()
    my_list = [int(el) for el in my_list]
    print([my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]])
except:
    print ('Введены неверные данные!')


