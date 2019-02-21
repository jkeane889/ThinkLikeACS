import turtle
import math
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.tracer(100)
wn.setworldcoordinates(-1,-1,1,1)

def quadmap():
    fred.up()
    fred.goto(-1, -1)
    fred.pendown()
    fred.goto(-1, 1)
    fred.goto(1, 1)
    fred.goto(1, -1)
    fred.goto(-1, -1)
    fred.goto(0, -1)
    fred.goto(0, 1)
    fred.goto(-1, 1)
    fred.goto(-1, 0)`
    fred.goto(1, 0)
    fred.penup()

def drawQuadCircle(x, y, anyTurtle, radius, numSides):
    anyTurtle.goto(x, y)
    anyTurtle.pendown()
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    turnAngle = 360 / numSides
    for i in range(numSides):
        anyTurtle.forward(sideLength)
        anyTurtle.right(turnAngle)
    anyTurtle.penup()

def throwDarts(anyTurtle, numdarts):
    insideCount = 0
    darts = numdarts

    for i in range(numdarts):
        x_point = random.random()
        randx_sign = random.randint(-1, 1)
        randx = x_point * randx_sign
        y_point = random.random()
        randy_sign = random.randint(-1, 1)
        randy = y_point * randy_sign

        x = randx
        y = randy

        anyTurtle.goto(x, y)
        x = anyTurtle.distance(0, 0)
        print(x)
        if x > 1:
            anyTurtle.dot(darts, "red")
        else:
            anyTurtle.dot(darts, "blue")
            insideCount = insideCount + 1

    pi = (insideCount/numdarts) * 4
    print(pi)


def main():
    quadmap()
    drawQuadCircle(0, 1, fred, 1, 360)
    throwDarts(fred, 10)

main()

wn.exitonclick()