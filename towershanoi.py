# Towers of Hanoi
'''
You have three disks of varying sizes (large, medium, small) - these disks are stacked on top
of one another on a single tower/rod.

Problem Rules:
1. Only one disk can be moved at a time
2. Each move consists of taking the upper disk from one of the stacks and placing it atop another stacks
3. No disk may be placed on top of a smaller disks

'''


def printMove(fr, to):
    print('move from' + str(fr) + 'to' + str(to))


def Towers(n, fr, to, spare):  # three towers, one named 'from', one named 'to', and one named 'spare'
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)


Towers(3, 1, 2, 3)
