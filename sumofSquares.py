xs = [3, 6, 5, 8, 50, 4739, 68403, 57, 304, 57, 205, 3759]


def sum_of_squares(n):
    total = 0
    for i in range(len(n)):
        n[i] = n[i] ** 2
    for i in n:
        total = total + i
    return total


print(sum_of_squares(xs))
