class OnlyInt (Exception):
    pass
my_list = []
while True:
    try:
        vvod = input('Введите число для добавления в список, чтобы выйти наберите "stop": ')
        if vvod == 'stop':
            break
        if not vvod.isdigit():
            raise OnlyInt()
        my_list.append(int(vvod))
    except OnlyInt:
        print('Введено не число!!!')
print (my_list)
