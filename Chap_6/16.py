import turtle
def star(n,turtlename):
    for i in range(n):
        turtlename.forward(100)
        turtlename.left(180-180/n)
wn=turtle.Screen()
alex=turtle.Turtle()
alex.speed(9)
star(7,alex)
wn.exitonclick()