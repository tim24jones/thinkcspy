class Point:
    def __init__(self,initX,initY):
        self.x=initX
        self.y=initY
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getslope(self,p):
        if self.x!=p.x:
            m=(self.y-p.y)/(self.x-p.x)
            return m
        else:
            return None
    def get_line_to(self,p):
        if self.getslope(p)==None:
            x=self.x
            print('line is vertical')
            return ('infinite',None)
        else:
            m=self.getslope(p)
            return (m,(self.y-self.x*m))

v=Point(2,3)
p=Point(2,5)
print(v.get_line_to(p))
