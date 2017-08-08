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
    def diagonal(self):
        diag=(self.w**2+self.h**2)**0.5
        return(diag)
r=Rectangle(Point(0,0),10,5)
print (r.diagonal())
