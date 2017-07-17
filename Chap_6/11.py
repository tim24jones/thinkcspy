import turtle
def drawPoly(someturtle, somesides, somesize):
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)
def drawequitriangle(someturtle,somesize):
    drawPoly(someturtle,3,somesize)
wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color('blue')
drawequitriangle(alex,30)
wn.exitonclick()