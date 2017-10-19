def mySqrt(n):
    oldguess=n
    for i in range(200):
        newguess=(1/2)*(oldguess+(n/oldguess))
        oldguess=newguess
    return(newguess)
