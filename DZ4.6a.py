from itertools import count
from sys import argv
def my_func(name, start, end):
    for el in count(start):
        if el > end:
            break
        print (el)

name, start, end = argv

my_func(name, int(start), int(end))