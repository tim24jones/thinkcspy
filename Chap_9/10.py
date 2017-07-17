def count(substr,theStr):
	count=0
	for i in range(len(theStr)):
		if substr==theStr[i:i+len(substr)]:
			count=count+1
	return(count)