import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.speed(10)
tess.stamp()
tess.up()
for i in range(12):
    tess.forward(70)
    tess.down()
    tess.forward(10)
    tess.up()
    tess.forward(15)
    tess.stamp()
    tess.up()
    tess.left(180)
    tess.forward(95)
    tess.left(360/12)
wn.exitonclick()