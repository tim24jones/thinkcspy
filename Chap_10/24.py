def sumUntilEven(lst):
    sumlist=0
    a=0
    for i in range(len(lst)):
        if lst[i]%2!=0 and a!=1:
            sumlist=sumlist+lst[i]
        else:
            a=1
    return(sumlist)