def remove_dups(astring):
    newstring=''
    usedchars=''
    for i in range(len(astring)):
        if astring[i] in usedchars:
            usedchars=usedchars+astring[i]
        else:
            newstring=newstring+astring[i]
            usedchars=usedchars+astring[i]
    #print("newstring=",newstring)
    #print("usedchars=",usedchars)
    return(newstring)
print(remove_dups("mississippi"))   #should print misp