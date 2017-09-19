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
        return self.h
    def getWidth(self):
        return self.w
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
        corner_point_list=[]
        corner_point_list=[Point(self.place.x,self.place.y),Point(self.place.x+self.w,self.place.y),Point(self.place.x,self.place.y+self.h),Point(self.place.x+self.w,self.place.y+self.h)]
        return corner_point_list
    def rect_is_in(self,otherrect):
        #if corner_points(self) are all greater or all less than corner points of other wrt either x or y, then true, otherwise false.
        initialx=0
        initialy=0
        selfcorners=self.corner_points()
        othercorners=otherrect.corner_points()
        for n in range(3):
            if selfcorners[n].x<othercorners[n].x and initialx==(0 or -1):
                initialx=-1
            else:
                return "rectangles overlap"
            if selfcorners[n].x>othercorners[n].x and initialx==(0 or 1):
                initialx=1
            else:
                return "rectangles overlap"

            if selfcorners[n].y<othercorners[n].y and initialy==(0 or -1):
                initialy=-1
            else:
                return "rectangles overlap"
            if self.corners[n].y>othercorners[n].y and initialy==(0 or 1):
                initialy=1
            else:
                return "rectangles overlap"
        return "rectangles do not overlap"

r=Rectangle(Point(0,0),1,2)
q=Rectangle(Point(4,7),3,3)
print(q.rect_is_in(r))
