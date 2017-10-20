def mirror(mystr):
    mirr=""
    for item in mystr:
        mirr=item+mirr
    mirr=mystr+mirr
    return(mirr)
mirror('abcde')
