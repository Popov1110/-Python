with open('dz5_4.txt', 'r', encoding="utf-8") as text:
    my_list = [line for line in text]
    my_list[0] = my_list[0].replace ('One', 'Один')
    my_list[1] = my_list[1].replace('Two', 'Два')
    my_list[2] = my_list[2].replace('Three', 'Три')
    my_list[3] = my_list[3].replace('Four', 'Четыре')
with open ('dz5_4_new.txt', 'w') as text_new:
    text_new.writelines(my_list)
