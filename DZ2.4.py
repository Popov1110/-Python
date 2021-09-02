text = input('Введите текст:')
text = text.split(' ')
for i in range(len(text)):
    print (f'{i+1}.{text[i][:10]}')