class Point:
    def __init__(self,initX,initY):
        self.x=initX
        self.y=initY
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def slope_from_origin(self):
        return self.y/self.x
v=Point(2,3)
print(v.slope_from_origin())