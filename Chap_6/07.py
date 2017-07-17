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

n=5
m=0
for j in range(5):
    drawSquare(alex,20+m)
    alex.penup()
    alex.backward(n)
    alex.right(90)
    alex.forward(n)
    alex.left(90)
    alex.pendown()
    m=m+2*n
wn.exitonclick()