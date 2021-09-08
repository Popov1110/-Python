from itertools import cycle
from sys import argv
def my_func(name, text, end):
    с = 0
    for el in cycle(text):
        if с > int(end):
            break
        print(el)
        с += 1
name, text, end = argv
my_func(name, text, end)