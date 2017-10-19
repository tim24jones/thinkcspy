import turtle
def star(turtlename):
    turtlename.left (108)
    for i in range(5):
        turtlename.forward(100)
        turtlename.left(180-36)
wn=turtle.Screen()
wn.bgcolor("lightgreen")
alex=turtle.Turtle()
alex.color('hot pink')
alex.speed(9)
alex.penup()
alex.right(60)
alex.forward(170)
alex.left(60)
alex.pendown()
for i in range(5):
    star(alex)
    alex.penup()
    alex.forward(350)
    alex.right(324)
    alex.pendown()
wn.exitonclick()
