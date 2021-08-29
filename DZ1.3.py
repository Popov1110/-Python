try:
    n = input ("Введите число:")
    sum = int(n) + int(n+n) + int(n+n+n)
    print (sum)
except:
    print("Введены неверные данные!")
