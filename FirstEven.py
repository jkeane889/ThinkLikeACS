import random


def sum(lst):
    sum = 0
    index = 0
    while index < len(lst) and lst[index] % 2 != 0:
        sum = sum + lst[index]
        index = index + 1
    return sum


lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(sum(lst))
