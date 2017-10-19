import turtle
def fancySquare(someturtle):
    for i in range(4):
        someturtle.forward(60)
        someturtle.left(90)
        drawSprite(someturtle,3,20)
def drawSprite(someturtle,legnumber,leglength):
    someturtle.shape("circle")
    someturtle.speed(10)
    someturtle.stamp()
    someturtle.down()
    for i in range(legnumber):
        someturtle.forward(leglength)
        someturtle.right(30)
        someturtle.forward(10)
        someturtle.left(120)
        someturtle.forward(10)
        someturtle.left(120)
        someturtle.forward(10)
        someturtle.right(30)
        someturtle.forward(leglength)
        someturtle.left(180)
        someturtle.left(360/legnumber)
atchoo=turtle.Turtle()
wn=turtle.Screen()
fancySquare(atchoo)
wn.exitonclick()
