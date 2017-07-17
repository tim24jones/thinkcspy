def myPi(iters):
	x=0
	for i in range(iters):
		x=x+(1/(4*i+1))-(1/(4*i+3))
	return(4*x)
print(myPi(520000))