import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.left(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

def drawFilledCircle(anyTurtle, radius, color):
    turtle.color(color)
    turtle.begin_fill()
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)
    turtle.end_fill()

wn = turtle.Screen()
wheel = turtle.Turtle()

drawFilledCircle(wheel, 10, "red")

wn.exitonclick()
