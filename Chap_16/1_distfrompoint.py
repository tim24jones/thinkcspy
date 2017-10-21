class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    def distanceFromPoint(Point,self):
        return((((Point.x-self.x)**2)+((Point.y-self.y)**2))**0.5)


p = Point(7, 6)
v=Point(2,1)
print(p.distanceFromOrigin())
print(p.distanceFromPoint(v))
