import turtle
def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.left(90)               # Point up
    if (height>=200):
        t.fillcolor('red')
    elif (height>=100 and height<200):
        t.fillcolor('yellow')
    elif (height<100):
        t.fillcolor('green')
    else:
        print('fillcolor error')
    t.begin_fill()
    t.forward(height)        # Draw up the left side
    t.right(90)
    t.forward(40)            # width of bar, along the top
    t.right(90)
    t.forward(height)        # And down again!
    t.right(90)
    t.forward(40)
    t.end_fill()
    t.right(180)
    t.forward(40)
wn=turtle.Screen()
xs=[48, 117, 200, 240, 160, 260, 220]
tess=turtle.Turtle()
tess.speed(9)
tess.penup()
tess.backward(200)
tess.right(90)
tess.forward(100)
tess.left(90)
tess.pendown()
for v in xs:                 # assume xs and tess are ready
    drawBar(tess, v)
wn.exitonclick()    
