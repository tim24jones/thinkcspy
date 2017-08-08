import math
class Point:
    def __init__(self,initX,initY):
        self.x=initX
        self.y=initY
    def getX(self):
        return self.x
    def getY(self):
        return self.y
class Rectangle:
    def __init__(self,corner_point,width,height):
        self.w=width
        self.h=height
        self.place=corner_point
    def getHeight(self):
        return self.w
    def getWidth(self):
        return self.h
    def __str__(self):
        return "width=" + str(self.w) + ", height=" + str(self.h)
    def area(self):
        return(self.w*self.h)
    def perimeter(self):
        return(2*self.w+2*self.h)
    def transpose(self):
        return(Rectangle(self.place,self.h,self.w))
    def contains(self,point):
        if ((point.x>=self.place.x and point.x<(self.place.x+self.w)) and (point.y>=self.place.y and point.y<(self.place.y+self.h))):
            return(True)
        else:
            return(False)
r=Rectangle(Point(0,0),10,5)
a=Point(0,0)
b=Point(3,3)
c=Point(3,7)
d=Point(3,5)
e=Point(3,4.99999)
f=Point(-3,-3)
print (r.contains(a))
print (r.contains(b))
print (r.contains(c))
print (r.contains(d))
print (r.contains(e))
print (r.contains(f))