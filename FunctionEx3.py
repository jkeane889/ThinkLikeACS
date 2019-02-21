import turtle

def drawRectangle(t, w, h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def drawSquare(tx, sz):
    drawRectangle(tx, sz, sz)  #when drawSquare(tess, 50) is called below, "sz" is denoted as the same value in the drawRectangle function called within the drawSquare function

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

drawSquare(tess, 50)

wn.exitonclick()