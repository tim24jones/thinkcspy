#a
def countlist(list,item):
    count=0
    for i in range(len(list)):
        if list[i]==item:
            count=count+1
        else:
            count=count
    return(count)
print(countlist([2,5,9,3,2,2,1],2))
#b
def inlist(list,item):
    count=False
    for i in range(len(list)):
        if list[i]==item:
            count=True
        else:
            count=count
    return(count)
print(inlist([2,5,9,3,2,2,1],-2))
#c
def reverse(list):
    newlist=[]
    for i in range(len(list)):
        newlist=[list[i]]+newlist
    return(newlist)
print(reverse([2,5,9,3,2,2,1]))
#d
def index_list(list,index):
    if index<=len(list):
        return(list[index])
    else:
        return('list not that long')
print(index_list([2,5,9,3,2,2,1],4))
#e
def list_insert(list,position,item):
    new_list=[]
    if position>len(list)+1:
        return('Position too high')
    for i in range(len(list)):
        if i<position:
            new_list=new_list+[list[i]]
            print(new_list)
        elif i==position:
            new_list=new_list+[item]
            new_list=new_list+[list[i]]
        else:
            new_list=new_list+[list[i]]
    return(new_list)
print(list_insert([2,5,9,3,4,2,1],4,"hello"))