try:
    a = int(input("Введите целое положительное число:"))
    if a < 0:
        print("Сказано же: целое положительное число!!!")
    else:
        max = 0
        while a > 10:
            i = a % 10
            a //= 10
            if i > max:
                max = i
        print(max)
except:
    print ("Сказано же: целое положительное число!!!")

