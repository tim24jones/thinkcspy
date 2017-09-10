import turtle

def createLSystem(numIters,axiom):
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
    if ch == 'F':
        newstr = 'F[-F]F[+F]F'   # Rule 1
    #elif (put other rules here with more elifs if necessary)
    else:
        newstr = ch    # no rules apply so keep the character
    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    aTurtle.speed(0)
    savedInfoList=[]
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
            print(savedInfoList)
        elif cmd == ']':
            newInfo = savedInfoList.pop()
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1], newInfo[2])
            #print(newInfo)
            #print(savedInfoList)


def main():
    inst = createLSystem(3, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(100)
    t.down()

    drawLsystem(t, inst, 25, 5)   # draw the picture
                                  # angle 25, segment length 5
    wn.exitonclick()

main()
