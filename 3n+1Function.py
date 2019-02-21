import math
import turtle

def turtleGraph(t):
    t.up()
    t.goto(0, 0)
    t.pendown()
    t.pensize(1)
    for i in range(4):
        t.forward(500)
        t.left(90)

def main():
    mofo = turtle.Turtle()
    wn = turtle.Screen()
    wn.tracer(100)
    wn.setworldcoordinates(0, 0, 500, 500)

    turtleGraph(mofo)

    def seq3np1(n):
        global count
        count = 0

        while n != 1:
            count = count + 1
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
        count = count + 1

        if n == 1:
            return n

    for start in range(1, 100000):
        seq3np1(start)
        result = start
        x = start
        y = count
        if y > 100:
            mofo.goto(start, count)
        else:
            continue

    maxSoFar = 0

    if count > maxSoFar:
        maxSoFar = count
        print(maxSoFar)
    else:
        maxSoFar = maxSoFar

    wn.exitonclick()
main()
