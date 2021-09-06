def my_func(x, y):
    return x**y
print (my_func(float(input('Введите число: ')), int(input('Введите степень: '))))


def my_func(x, y):
    z = 1
    for i in range(0,abs(y)):
        z *= x
    return 1/z
print (my_func(float(input('Введите число: ')), int(input('Введите степень: '))))