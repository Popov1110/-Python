my_list = input('Введите элементы списка через пробел: ').split()
print([ el for el in my_list if my_list.count(el) == 1])