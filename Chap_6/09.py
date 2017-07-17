import turtle
def drawSquare(someturtle, somesides, somesize):
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.speed(9)
for j in range (20):
    drawSquare(alex,4,40)
    alex.left(360/20)