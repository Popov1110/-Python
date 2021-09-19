with open('dz5_3.txt', 'r', encoding="utf-8") as text:
    vedomost = {}
    for line in text:
        vedomost [line.split(' ')[0]] = int(line.split(' ')[1].replace ('\n','' ))
    for key in vedomost:
        if int(vedomost[key]) < 20000: print (key)
    print (sum([*vedomost.values()])/len([*vedomost.values()]))