
my_list = []
ans = False

def summa(x):
    global my_list, ans
    my_list += x.split()
    symbols = '!@#$%^&*()_-=+{}[]''""\/|?.,№<>~`'
    for el in symbols:
       if el in my_list:
           my_list.remove(el)
           ans = True
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    return  sum(my_list)

try:
    while ans == False:
        y = summa(input('Введите числа через пробел, для завершения введите любой спецсимвол: '))
        print(y)
except:
    print ('Введены неверные данные!')
