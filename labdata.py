import turtle
infile = open("C:/Users/jkean/Desktop/Programming/PycharmProjects/PythonTraining/labdata.txt", "r")


def plotRegression():
    n = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, 120, 120)
    n.goto(0, 0)
    n.speed(9)
    n.down()
    n.forward(100)
    n.backward(100)
    n.left(90)
    n.forward(100)
    n.backward(100)
    n.up()
    line = infile.readline()
    while line:
        values = line.split()
        tolx = 0
        toly = 0
        xcnt = 0
        ycnt = 0
        for i in values[0]:
            tolx = tolx + int(i)
            xcnt = xcnt + 1
        for i in values[1]:
            toly = toly + int(i)
            ycnt = ycnt + 1
        for i in values:
            n.goto(int(values[0]), int(values[1]))
            n.dot(5, "black")
            n.up()
        line = infile.readline()

    x1 = 8
    x2 = 90

    m1 = (((tolx) * (toly)) - (xcnt * ((tolx / xcnt) * (toly / ycnt))))
    m2 = ((tolx ** 2) - (xcnt * (tolx ** 2)))
    m3 = m1 / m2

    y1 = ((toly / ycnt) + m3 * (x1 - (tolx / xcnt)))

    y2 = ((toly / ycnt) + m3 * (x2 - (tolx / xcnt)))

    n.goto(x1, y1)
    n.pendown()
    n.pencolor("pink")
    n.goto(x2, y2)
    n.up()

    wn.exitonclick()
    infile.close()


plotRegression()
