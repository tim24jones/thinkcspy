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
r=Rectangle(Point(4,5),6,5)
print(r.perimeter())
