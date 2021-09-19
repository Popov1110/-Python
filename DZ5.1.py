with open('dz5_1.txt', 'w') as zametki:
    text = ''
    while text != '\n':
        text = input('Введите строку или нажмите Enter для выхода:') + '\n'
        zametki.write(text)
