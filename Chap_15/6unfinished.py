def hanoi(hoops)
    rod1=[]
    rod2=[]
    rod3=[]
    for i in range(hoops)
        rod1=[i]+rod1 #set up situation
    print(rod1)

def move(fromrod,torod)
    if fromrod[-1]<torod[-1]:
        torod=torod+[fromrod[-1]]
        fromrod=fromrod[:-1]
        return(fromrod,torod)#return new arrangements
    else:
        return(0)#move invalid
def trymoves(rod1,rod2,rod3,hoops)
    if move(rod1,rod2)==0:
        if move (rod1,rod3)==0:
            if move rod2,rod3)==0:
                move (rod3,rod2)
            else:
                move (rod2,rod3)
        else:
            move (rod1,rod3)
    else:
        move (rod1,rod2)
    

