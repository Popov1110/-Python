goods = []
ans = '+'
while ans == '+':
    my_dict = {'Название': None, 'Цена': None, 'Количество': None, 'Ед': None}
    goods.append((input('Введите номер товара: '), my_dict))
    my_dict['Название'] = input('Введите название товара: ')
    my_dict['Цена'] = input('Введите цену товара: ')
    my_dict['Количество'] = input('Введите количество товара: ')
    my_dict['Ед'] = input('Введите единицы измерения: ')
    ans = input('Для того чтобы ввести новый элемент нажмите "+", чтобы выйти нажмите любую другую клавишу')

anal = {'Название': None, 'Цена': None,'Количество': None, 'Ед': None}
print()
print(*goods, sep= '\n')
anal_naz = []
anal_price = []
anal_am = []
anal_ed = []
for el in goods:
    anal_naz.append(el[1]['Название'])
    anal_price.append(el[1]['Цена'])
    anal_am.append(el[1]['Количество'])
    anal_ed.append(el[1]['Ед'])

anal['Название'] = anal_naz
anal['Цена'] = anal_price
anal['Количество'] = anal_am
anal['Ед'] = anal_ed
print()
for key, value in anal.items():
    print(f'"{key}" : {value}')












