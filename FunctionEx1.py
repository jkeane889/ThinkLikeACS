import turtle

def drawMulticolorSquare(t, sz):

    for i in ['red', 'purple', 'hotpink', 'blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

size = 20
for i in range(15):
    drawMulticolorSquare(tess, size)
    size = size + 10
    tess.forward(10)
    tess.right(18)

wn.exitonclick()