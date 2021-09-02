my_list = [7, 5, 3, 3, 2]
ans = '+'
while ans == '+':
    new_el = int(input('Введите новый элемент: '))
    my_list.append(new_el)
    my_list.sort(reverse=True)
    print(*my_list, sep=', ')
    ans = input('Для того чтобы ввести новый элемент нажмите "+", чтобы выйти нажмите любую другую клавишу')
