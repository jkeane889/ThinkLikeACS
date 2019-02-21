import random

randList = []
for item in range(100):
    n = int(random.randrange(0, 1000))
    randList = randList + [n]

print(randList)


def average(n):
    '''average = total of list integers divided by count of list integers '''
    averageList = 0
    for i in n:
        averageList = averageList + i

    randaverage = averageList / len(n)
    return randaverage


def maxValue(m):
    x = m[0]
    for value in m:
        if value > x:
            x = value
    return x


print(average(randList))
print(maxValue(randList))
