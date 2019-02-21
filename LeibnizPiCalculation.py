import math

def myPi(iters):
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign/denominator)  # 1 = 0 + 1, .667 = 1 + (-1/3), .867 = .667 + (1/5)
        sign = sign * -1              # -1 = 1 * -1, 1 = -1 * -1, 
        denominator = denominator + 2 # 3 = 1 + 2, 5 = 3 + 2

    pi = pi * 4
    return pi

pi_approx = myPi(10000)
print(pi_approx)