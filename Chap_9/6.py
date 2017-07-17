def reverse(astring):
    rever=""
    for item in astring:
        rever=item+rever
    return(rever)
reverse('abcde')