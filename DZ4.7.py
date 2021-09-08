from itertools import count
from math import factorial

def my_func():
    for i in count(1):
        yield factorial(i)

try:
    n = int(input('Введите число n: '))
    j = 0
    for el in my_func():
        if j < n:
            print(el)
            j += 1
        else:
            break
except:
    print ('Введены неверные данные!')
