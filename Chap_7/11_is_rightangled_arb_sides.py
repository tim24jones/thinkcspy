def is_rightangled(a, b, c):
    if (a>b):
        hyp=a
    else:
        hyp=b
    if (c>hyp):
        d=(a**2+b**2)**0.5
        if (abs(d-c)<0.0001):
            return(True)
        else:
            return(False)
    elif (hyp==a):
        d=(b**2+c**2)**0.5
        if (abs(d-a)<0.0001):
            return(True)
        else:
            return(False)
    elif (hyp==b):
        d=(a**2+c**2)**0.5
        if (abs(d-b)<0.0001):
            return(True)
        else:
            return(False)
    else:
        return(False)
