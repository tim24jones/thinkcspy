import turtle
def drawPoly(someturtle, somesides, somesize):
	for i in range(somesides):
		someturtle.forward(somesize)
		someturtle.left(360/somesides)

wn=turtle.Screen()
wn.bgcolor("lightgreen")
Matt=turtle.Turtle()
Matt.color('hotpink')
Matt.pensize(3)
drawPoly(Matt, 4, 30)
wn.exitonclick()
