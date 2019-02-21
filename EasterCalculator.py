import math

def easter(n):

    a = n % 19
    b = n % 4
    c = n % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date_of_easter = 22 + d + e

    if n < 1900 or n > 2099:
        print("Please try again")
        n = input("Please enter a year between 1900 and 2099: ")
    else:
        print("The date of Easter in year ", n, "is: ", date_of_easter)

easter(2100)