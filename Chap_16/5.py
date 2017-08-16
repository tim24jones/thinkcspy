class Point:
    def __init__(self,initX,initY):
        self.x=initX
        self.y=initY
    def __str__(self):
        return '(',self.x,',',self.y,')'
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def move(self,dx,dy):
        return Point(self.x-dx,self.y-dy)
v=Point(3,5)
print(v.move(2,3))