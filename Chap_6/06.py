import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("deep pink")

for j in range(5):
    alex.width(2)
    drawSquare(alex,20)
    alex.penup()
    alex.forward(40)
    alex.pendown()

wn.exitonclick()