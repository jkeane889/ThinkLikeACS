import random

lst1 = []
for i in range(100):
    lst1.append(random.randint(0, 1000))
print(lst1)
lst1.reverse()
print(lst1)

lst2 = []
for i in range(100):
    lst2.append(random.randint(0, 1000))
print(lst2)
lst2.reverse()
print(lst2)


def listMethods(n, m):
    index = 0
    duplicate = 0
    while index < len(n):
        for i in n:
            if i in m:
                duplicate = duplicate + 1
                return m.index(i)
            elif i not in m:
                m.insert(100, i)
            index = index + 1
    print(m.index(i))


print(listMethods(lst1, lst2))
