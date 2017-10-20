def remove(substr,theStr):
    count=0
    rmStr=''
    for i in range(len(theStr)):
        if(count==1):
            rmStr=rmStr
        elif substr==theStr[i:i+len(substr)]:
            rmStr=theStr[:i]+theStr[i+len(substr):]
            count=1
    if count==0:
        rmStr=theStr
    return(rmStr)
