def salary (name, time, price, bonus):
    return float(time) * float(price) + float(bonus)
from sys import argv
name, time, price, bonus = argv
print(salary(name, time, price, bonus))
