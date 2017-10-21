import turtle
fileref=open("mystery.txt",'r')
wn=turtle.Screen()
wn.setworldcoordinates(-325,-300,400,250)
t=turtle.Turtle()
for aline in fileref:
    values=aline.split()
    if values==['UP']:
        t.penup()
    elif values==['DOWN']:
        t.pendown()
    else:
        #print(values)
        t.goto(int(values[0]),int(values[1]))
wn.exitonclick()
fileref.close()
