
def int_func(text):
    return text.title()
ans = '+'
while ans == '+':
    print(int_func(input('ведите текст: ')))
    ans = input('Хотите ввести текст? (для продолжения нажмите "+", для выхода любую другую кнопку): ')