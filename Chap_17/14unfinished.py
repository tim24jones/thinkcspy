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
    def corner_points(self):
        [corner_point,Point(corner_point.x+self.w,corner_point.y),Point(corner_point.x,corner_point.y+self.h),Point(corner_point.x+width,corner_point.y+height)]
    def rect_is_in(self,otherrect):
        #if corner_points(self) are all greater or all less than corner points of other wrt either x or y, then true, otherwise false.
        initialx=0
        initialy=0
        for n in range(3)
            if self.corner_points[n].x<otherrect.corner_points[n].x and initialx=(0 or -1)
                initialx=-1
            else:
                return "rectangles overlap"
            if self.corner_points[n].x>otherrect.corner_points[n].x and initialx=(0 or 1):
                initialx=1
            else:
                return "rectangles overlap"

            if self.corner_points[n].y<otherrect.corner_points[n].y and initialy=(0 or -1)
                initialy=-1
            else:
                return "rectangles overlap"
            if self.corner_points[n].y>otherrect.corner_points[n].y and initialy=(0 or 1):
                initialy=1
            else:
                return "rectangles overlap"
        return "rectangles do not overlap"

#r=Rectangle(Point(0,0),10,5)
#print (r.diagonal())