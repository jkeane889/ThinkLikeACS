import math

def leapYear(n):
    if n % 4 == 0:
        print("This is a leap year.")
    elif n % 100 == 0 and n % 400 == 0:
        print("This is a leap year.")
    else:
        print("This is not a leap year.")

leapYear(2020)