def remove_all(substr,theStr):
	count=0
	rmStr=''
	chngstr=theStr
	i=0
	while i<len(chngstr):
		if substr==chngstr[i:i+len(substr)]:
			rmStr=chngstr[:i]+chngstr[i+len(substr):]
			chngstr=rmStr
			i=i+1
	if count==0:
		rmStr=theStr
    return(rmStr)