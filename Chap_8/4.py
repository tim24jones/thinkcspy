import random
import turtle
#def isInScreen(w, t):
#    if random.random() > 0.1:
#        return True
#    else:
#        return False
t = turtle.Turtle()
wn = turtle.Screen()
t.shape('turtle')
n=1
while (n==1):
    coin = random.randrange(0, 360)
    t.left(coin)
    t.forward(50)
wn.exitonclick()