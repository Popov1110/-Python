class OnZero (Exception):
    pass
b = 0
while b == 0:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        if b == 0:
            raise OnZero()
        print (a/b)
    except OnZero:
        print('Деление на ноль запрещено!!!')
