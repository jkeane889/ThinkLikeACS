import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "green"]:  #repeat 4 times
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()