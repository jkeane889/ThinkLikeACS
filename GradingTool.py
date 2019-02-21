import math

def gradeScale():
    for i in [56, 84, 90, 45, 88, 79, 90, 95]:
        if i >= 90:
            print(i, "- You received an A - congratulations!")
        elif i >= 80 and i < 90:
            print(i, "- You received a B - congrats!")
        elif i >= 70 and i <80:
            print(i, "- You received a C - good job!")
        elif i >= 60 and i <70:
            print(i, "- You received a D - passed.")
        elif i <= 60:
            print(i, "- You failed.")
        else:
            continue

gradeScale()