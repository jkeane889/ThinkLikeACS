# koch triangle/iterative mountain
import turtle


def koch_0(t, size):
    t.forward(size)


def koch_1(t, size):
    for angle in [60, -120, 60, 0]:
        koch_0(t, size / 3)
        t.left(angle)


def koch_2(t, size):
    for angle in [60, -120, 60, 0]:
        koch_1(t, size / 3)
        t.left(angle)


def koch_3(t, size):
    for angle in [60, -120, 60, 0]:
        koch_2(t, size / 3)
        t.left(angle)


def main():
    tess = turtle.Turtle()
    myWin = turtle.Screen()
    koch_3(tess, 200)
    myWin.exitonclick()


main()
