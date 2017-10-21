def computeFactorial(number):
    if number>=0:
        n=1
        for i in range(number):
            n=n*(i+1)
    else:
        n=None
    return(n)
print(computeFactorial(5))
