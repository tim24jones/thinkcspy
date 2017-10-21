import math
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
            return float(m)
        else:
            return None

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

    def get_line_to(self,p):
        if self.getslope(p)==None:
            x=self.x
            print('line is vertical')
            return ('infinite',None)
        else:
            m=self.getslope(p)
            return (m,(self.y-self.x*m))
def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

v=Point(3,4)
p=Point(2,5)
r=Point(1,7)
pt_1=p.halfway(v)
pt_2=p.halfway(r)
m_1=-1/float(p.getslope(v))
m_2=-1/float(p.getslope(r))
x_center=(pt_1.y-m_1*pt_1.x-pt_2.y+m_2*pt_2.x)/(m_2-m_1)
y_center=(m_1*m_2*(pt_2.x-pt_1.x)+m_1*pt_2.y+m_2*pt_1.y)/(m_2-m_1)
center=Point(x_center,y_center)
radius=distance(center,v)
print('(',x_center,',',y_center,')',radius)
