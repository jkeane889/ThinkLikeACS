lst = ["cattle", "time", "farms", "hello", "flats", "yacht"]


def fivewords(n):
    count = 0
    for i in n:
        if len(i) == 5:
            count = count + 1
    return count


print(fivewords(lst))
