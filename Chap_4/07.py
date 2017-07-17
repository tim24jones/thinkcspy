import turtle
wn=turtle.Screen()
bob=turtle.Turtle()
heading=0
for angle in [160,-43,270,-97,-43,200,-940,17,-86]:
    bob.forward(100)
    bob.left(angle)
    heading=heading+angle
print("The current heading is", 360%heading)
print("The current heading is", bob.heading())
wn.exitonclick()