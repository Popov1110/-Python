try:
    v = int (input ("Сколько выручка?"))
    i = int (input ("Сколько издержки?"))

    if v > i:
        r = (v - i) / v * 100
        print (f"Так держать! Вы в плюсе! Рентабельность {r}%")
        p = int (input("Сколлько у вас сотрудников?"))
        z = (v-i) / p
        print (f"Вы заработали по {z} на каждого!")
    elif v == i:
        print("Какой-то бестолковый бизнес, прибыль нулевая!")
    else:
        print ("Ваше дело труба!!!")
except:
    print("Вы ввели неверные данные!")
