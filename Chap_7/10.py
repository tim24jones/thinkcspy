def is_rightangled(a, b, c):
    d=(a**2+b**2)**0.5
    if abs(d-c)<0.0001:
        return(True)
    else:
        return(False)