def count(p):
    a=0
    t=0
    for i in range (len(p)):
        if p[i]=='e':
            a=a+1
            t=t+1
        else:
            t=t+1
    print('Your text contains', t, 'alphabetic characters, of which', a, ' (', round(100*a/t,1), "%) are 'e'.")
p='Once when I was but a little bitty boy, and a heigh ho, the wind and the rain, oh the rain it reigns most every day'
count(p)