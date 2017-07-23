def countOdd(lst):
    newlist=[]
    for i in range(len(lst)):
        if lst[i]%2==1:
            newlist=newlist+[lst[i]]
    return(len(newlist))