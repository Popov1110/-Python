my_list = []
opros = '+'
while opros == '+':
    el = input ('Введите элемент списка ')
    my_list.append(el)
    print(f'Список имеет вид: {my_list}')
    opros = input ('Чтобы добавить элемент в список нажмите +, чтобы продолжить нажмите любую другую клавишу ')

i = 0
while i < len(my_list)-1 :
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2


print(my_list)