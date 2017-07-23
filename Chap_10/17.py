import random
mylist=[]
for i in range(100):
    mylist.append(random.randint(0,1000))
def average(myList):
    myListsum=0
    for i in range(100):
        myListsum=myListsum+myList[i]
    average=myListsum/100
    print(average)
    return(average)
average(mylist)
