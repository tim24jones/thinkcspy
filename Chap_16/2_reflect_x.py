class Point:
    def __init__(self,initX,initY):
        self.x=initX
        self.y=initY
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def reflect_x(self):
        return Point(self.x,-1*self.y)
v=Point(2,3)
print(v.reflect_x())
