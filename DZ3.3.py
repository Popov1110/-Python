def my_func(x, y, z):
    my_list = [x , y, z]
    my_list.sort(reverse = True)
    sum = my_list[0] + my_list[1]
    return  sum
print (my_func(float(input('Введите первое число: ')), float(input('Введите второе число: ')), float(input('Введите третье число: '))))