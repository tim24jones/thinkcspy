import turtle
def drawSprite(someturtle,legnumber,leglength):
    someturtle.shape("circle")
    someturtle.speed(10)
    someturtle.stamp()
    someturtle.down()
    for i in range(legnumber):
        someturtle.forward(leglength)
        someturtle.left(180)
        someturtle.forward(leglength)
        someturtle.left(180)
        someturtle.left(360/legnumber)
atchoo=turtle.Turtle()
wn=turtle.Screen()
drawSprite(atchoo,15,120)
wn.exitonclick()
