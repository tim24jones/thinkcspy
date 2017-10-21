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
    def getH(self):
        return self.w
    def getW(self):
        return self.h
r=Rectangle(Point(4,5),6,5)
print(type(r))
