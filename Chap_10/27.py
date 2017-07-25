def replace(s, old, new):
    slist=s.split(old)
    slist=s.split(old)
    
    print(slist)
    print(s)
    print(len(s))
    newstr=''
    alteredstr=''.join(slist)
    print(''.join(slist))
    a=0
    for i in range(len(s)):
        if i-a<len(alteredstr):
            if alteredstr[i-a]==s[i]:
                newstr=newstr+alteredstr[i-a]
                print(newstr)
            else:
                newstr=newstr+new
                print(newstr)
                a=a+1
        else:
            newstr=newstr+new
    return(newstr)