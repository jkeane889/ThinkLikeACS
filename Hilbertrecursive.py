import turtle

size = 10
w = turtle.Turtle()
wn = turtle.Screen()
turtle.color("blue")
turtle.speed(9)


def hilbert(level, angle):
    if level == 0:
        return

    w.right(angle)
    hilbert(level - 1, -angle)
    w.forward(size)
    w.left(angle)
    hilbert(level - 1, angle)
    w.forward(size)
    hilbert(level - 1, angle)
    w.left(angle)
    w.forward(size)
    hilbert(level - 1, -angle)
    w.right(angle)

    wn.exitonclick()


hilbert(10, 90)
