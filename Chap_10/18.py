import random
mylist=[]
for i in range(100):
    mylist.append(random.randint(0,1000))
def maximum(myList):
    myListmax=myList[0]
    for i in range(100):
        if myListmax<myList[i]:
            myListmax=myList[i]
        else:
            myListmax=myListmax
    return(myListmax)
print(maximum(mylist))