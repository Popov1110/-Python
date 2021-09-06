def delenie(x,y):
    z = x/y
    return z
try:
    print(delenie(float(input('Введите первое число: ')), float(input('Введите второе число: '))))
except ZeroDivisionError:
    print('На 0 делить нельзя')
except:
    print ('Введены неверные данные!')
