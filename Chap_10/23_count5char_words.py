def countWords(lst):
    a=0
    for i in range(len(lst)):
        if len(lst[i])==5:
            a=a+1
        else:
            a=a
    return(a)
myList=[]
print(countWords(myList))
