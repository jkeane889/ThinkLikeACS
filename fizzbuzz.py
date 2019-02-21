# FizzBuzz solution

"""The solution below takes an input integer "x", and enters it into a for loop.

Using the range function, we loop through each integer, starting at 1, and going up
to and INCLUDING "x" (we do this by adding a one to "x").  If we didn't add a 1 to "x",
the loop would stop right before "x."

The if statement starts with first determing if we have an integer that is both divisible by 3 and 5.
The modulus operator asks, "If I divide this number by 3, and get a remainder equal to zero, that means
that this number is divisible by 3."  We then ask the same thing regarding the number 5.  If the integer
is divisible by both 3 and 5, we return the statement "Fizz Buzz."

The subsequent conditionals then determine whether the number is only divisble by 3 or only divisible by 5,
thus returning either Fizz OR Buzz.  And if the integer is not divisible by any, we simply return the integer
with the else statement.

"""


def fizz_buzz(x):
    for i in range(1, x + 1):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)


fizz_buzz(15)
