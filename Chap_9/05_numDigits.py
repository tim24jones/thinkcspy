def numDigits(n):
    m=n
    a=1
    while (m%10!=m):
        m=m/10
        a=a+1
    return(a)
numDigits(3034)
