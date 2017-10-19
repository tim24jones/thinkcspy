def is_prime(n):
    b=0
    if (n<1):
        return('Prime numbers defined for positive integers, number too small')
    elif ((n==2) or (n==1)):
        return(True)
    else:
        for i in range (2,n):
            if(n%i==0):
                b=1
        if (b==1):
            return(False)
        else:
            return(True)
