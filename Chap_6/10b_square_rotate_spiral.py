import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
alex=turtle.Turtle()
alex.color("blue")
alex.speed(9)
alex.left(180)
n=2
for i in range(82):
	alex.forward(n)
	alex.right(89)
	n=n+2

wn.exitonclick()
