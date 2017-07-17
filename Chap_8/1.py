def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
        print(approx)
    return betterapprox

print(newtonSqrt(10, 25))