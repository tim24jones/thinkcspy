def is_palindrome(myStr):
    if myStr==reverse(myStr):
        return True
    else:
        return False
def reverse(astring):
    rever=""
    for item in astring:
        rever=item+rever
    return(rever)

