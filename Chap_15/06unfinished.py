def moveTower(height,fromPole, toPole, withPole):
    listfromPole=range(height)
    listtoPole=[]
    listwithPole=[]
    if height >= 1:
        #print(listfromPole,listwithPole,listtoPole)
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole,listfromPole,listtoPole)
        print(listfromPole,listwithPole,listtoPole)
        moveTower(height-1,withPole,toPole,fromPole)
        #print(listfromPole,listwithPole,listtoPole)
        
def moveDisk(fp,tp,lfp,ltp):
    print("moving disk from",fp,"to",tp)
    moving_disk=lfp.pop()
    ltp.append(moving_disk)

moveTower(3,"A","B","C")
