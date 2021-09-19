import json
from statistics import mean
with open ('DZ5_7.txt', 'r', encoding = 'utf-8') as spisok:
    my_dict = {}
    for line in spisok:
        my_dict[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
my_dictmid = {}
mid = [my_dict[key] for key in my_dict if my_dict[key] >= 0]
my_dictmid['average_profit'] = mean(mid)
ans = [my_dict, my_dictmid]
print (ans)
with open('DZ5_7.json', 'w') as new:
    json.dump(ans, new)

