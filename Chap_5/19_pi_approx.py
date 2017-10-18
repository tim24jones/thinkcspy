import math
i=10
p=0
for n in range (0,i,2):
    ad=(1/(4*n+1))
    ab=(1/(4*n+3))
    p=4*(ad-ab)+p
print(p)
print(math.pi)
