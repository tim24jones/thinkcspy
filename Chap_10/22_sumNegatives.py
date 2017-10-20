def sumNegatives(lst):
    sumnewlist=0
    for i in range(len(lst)):
        if lst[i]<=0:
            sumnewlist=sumnewlist+lst[i]
        else:
            sumnewlist=sumnewlist
    return(sumnewlist)
