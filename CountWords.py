names = ["julia", "harold", "william", "david", "sam"]


def countWords(n):
    count = 0
    index = 0
    while index < len(n) and n[index] != "sam":
        count = count + 1
        index = index + 1
    return count


print(countWords(names))
