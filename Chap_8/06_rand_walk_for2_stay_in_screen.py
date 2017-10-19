import turtle
import random

t1=turtle.Turtle()
t2=turtle.Turtle()
wn=turtle.Screen()

t1.penup()
t2.penup()

leftBound=-(wn.window_width()/2)
rightBound=wn.window_width()/2
topBound=wn.window_height()/2
bottomBound=-(wn.window_height()/2)

t1.setpos(random.randrange(leftBound,rightBound),random.randrange(bottomBound,topBound))
t2.setpos(random.randrange(leftBound,rightBound),random.randrange(bottomBound,topBound))

t1.pendown()
t2.pendown()

t1.speed(9)
t2.speed(9)

stillIn=True

def isInScreen(w,t1):
	if (t1.xcor()>rightBound or t1.xcor()<leftBound or t1.ycor()>topBound or t1.ycor()<bottomBound):
		stillIn=False
	else:
		stillIn=True
	return stillIn

def moveturtles(t1,t2):
    while(isInScreen(wn,t1) and isInScreen(wn,t2)):
        coin1=random.randrange(359)
        coin2=random.randrange(359)
        t1.left(coin1)
        t2.left(coin2)
        t1.forward(20)
        t2.forward(20)
while(stillIn):
    if (t1.xcor()==t2.xcor() and t1.ycor()==t2.ycor()):
        t1.left(180)
        t2.left(180)
    elif (isInScreen(wn,t1)==False):
        t1.left(180)
        t1.forward(20)
    elif (isInScreen(wn,t2)==False):
        t2.left(180)
        t2.forward(20)
    else:
        moveturtles(t1,t2)

wn.exitonclick()
