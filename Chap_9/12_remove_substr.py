def remove_all(substr,theStr):
    rmStr=''
    i=0
    while i<len(theStr):
        if substr==theStr[i:i+len(substr)]:
            rmStr=rmStr
            i=i+len(substr)
        else:
            rmStr=rmStr+theStr[i]
            i=i+1
    return(rmStr)
