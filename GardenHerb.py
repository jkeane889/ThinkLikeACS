import turtle


def createLsystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString


def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr


def applyRules(ch):
    newstr = ""
    if ch == "H":
        newstr = "HFX[+H][-H]"
    elif ch == "X":
        newstr = "X[-FFF][+FFF]FX"
    else:
        newstr = ch

    return newstr


def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == "F":
            aTurtle.forward(distance)
        elif cmd == "B":
            aTurtle.backward(distance)
        elif cmd == "+":
            aTurtle.right(angle)
        elif cmd == "-":
            aTurtle.left(angle)


def main():
    inst = createLsystem(5, "FXF--FF--FF")
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)

    wn.exitonclick


main()
