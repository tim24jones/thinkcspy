def count(lst):
    samcount=False
    wordcount=0
    for i in range(len(lst)):
        if samcount==False:
            wordcount=wordcount+1
            if lst[i]=="sam":
                samcount=True
        else:
            samcount=True
    return(wordcount)
print(count([]))