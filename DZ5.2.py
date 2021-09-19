with open('dz5_2.txt', 'r') as text:
    lines = 0
    for line in text:
        lines += 1
        words = len(line.split(' '))
        print(f'Слов в {lines} строке: {words}')
    print (f'Всего строк: {lines}')