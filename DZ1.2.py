
try:
    time = int(input("Введите время в секундах:"))

    h = time // 3600

    m = (time - h * 3600) // 60

    s = time - h*3600 - m*60

    print(f"{time} секунд - это: {h}ч {m}м {s}с")
except:
    print("Введены неверные данные!")
