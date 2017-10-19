import math
def myPi(iters):
    x=0
    for i in range(iters):
        x=((-1)**i/((1+2*i)*3**i))+x
    return(math.sqrt(12)*x)
print(myPi(9))
