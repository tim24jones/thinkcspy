import math
import turtle
sumx=0
sumy=0
n=0
xvalues=[]
yvalues=[]
sumxy=0
sumxsquared=0
fileref=open("labdata.txt",'r')
for aline in fileref:
    values=aline.split()
    xvalues=xvalues+[int(values[0])]#turning file into lists
    yvalues=yvalues+[int(values[1])]
    n=n+1 #counting number of points
xmax=xvalues[0]#initializing search for max x
xmin=xvalues[0]
ymax=yvalues[0]
ymin=yvalues[0]
for item in range(len(xvalues)):
    sumx=xvalues[item]+sumx #adding x values
    sumy=yvalues[item]+sumy
    sumxy=xvalues[item]*yvalues[item]+sumxy #creating terms for slope formula
    sumxsquared=xvalues[item]**2+sumxsquared
    if xvalues[item]>xmax:
        xmax=xvalues[item]#finding xmax
    if yvalues[item]>ymax:
        ymax=yvalues[item]#finding ymax
    if xvalues[item]<xmin:
        xmin=xvalues[item]
    if yvalues[item]<ymin:
        ymin=yvalues[item]
print(xmin,ymin,xmax,ymax)
xaverage=sumx/n
yaverage=sumy/n
slope=(sumxy-n*xaverage*yaverage)/(sumxsquared-n*xaverage**2)
#Draw regression line
wn=turtle.Screen()
wn.setworldcoordinates((xmin-10),(ymin-10),(xmax+10),(ymax+10))
t=turtle.Turtle()
t.penup()
t.setpos(xaverage,yaverage)#put turtle at known point on line
t.pencolor("red")
t.pendown()
angular_slope=math.degrees(math.atan(slope))
print(angular_slope)
t.left(angular_slope)
t.forward(50)
t.left(180)
t.forward(100)
t.penup()
t.pencolor("black")
t.shape("circle")
for i in range(n): #plot points
    t.goto(xvalues[i],yvalues[i])
    print(xvalues[i],yvalues[i],t.pos())
    t.pendown()
    t.stamp()
    t.penup()
    t.goto(0,0)
wn.exitonclick()
fileref.close()