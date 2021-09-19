with open ('DZ5.6.txt', 'r', encoding = 'utf-8') as spisok:
    my_dict = {}
    for line in spisok:
        my_dict[line.split(' ')[0][:-1]] = line.split(' ')[1:]
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for key in my_dict:
        for el in my_dict[key]:
            my_dict[key][my_dict[key].index(el)] = ''.join(i for i in el if i in num)
        for el in my_dict[key]:
            try:
                my_dict[key][my_dict[key].index(el)] = int(el)
            except:
                my_dict[key][my_dict[key].index(el)] = 0
        my_dict[key] = sum(my_dict[key])
    print(my_dict)
