import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

def drawBar(t, height):
    for i in height:
        t.begin_fill()
        if i >= 200:
            t.fillcolor("red")
        elif i >= 100 and i < 200:
            t.fillcolor("yellow")
        elif i < 100:
            t.fillcolor("green")
        t.left(90)
        t.forward(i)
        if i > 0:
            t.penup()
            t.forward(5)
            t.pendown()
            t.write(str(i))
            t.penup()
            t.backward(5)
            t.pendown()
        elif i < 0:
            t.penup()
            t.backward(i)
            t.pendown()
            t.write(str(i))
            t.penup()
            t.forward(i)
            t.pendown()
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(i)
        t.left(90)
        t.end_fill()

def main():
    xs = [48, -117, 200, -240, 160, 260, 220]
    drawBar(tess, xs)
    wn.exitonclick()

main()