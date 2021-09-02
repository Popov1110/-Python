month = int(input('Введите номер месяца:'))

# через dict
seasons = {'Зима' : (1, 2, 12), 'Весна' : (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

# через list
seasons = [(1, 2, 12), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
if month in seasons[0]:
    print ('Зима')
elif month in seasons[1]:
    print ('Весна')
elif month in seasons[2]:
    print ('Лето')
elif month in seasons[3]:
    print ('Осень')