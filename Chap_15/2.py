def reverseList(lst):
    newlist=[]
    for i in range(len(lst)):
        newlist=[lst[i]]+newlist
    return(newlist)
lst=['a','b',2,5]
print(reverseList(lst))