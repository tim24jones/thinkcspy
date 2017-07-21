def remove_dups(astring):
    newstring=''
    for i in range(len(astring)):
        if(astring[i] not in astring[:i]+astring[i+1:]):
            newstring=newstring+astring[i]
        else:
            newstring=newstring
    return(newstring)
print(remove_dups("mississippi"))