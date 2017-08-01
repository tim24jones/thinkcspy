def fibonacci(terms):
    f_list=[1]
    if terms<=0:
        print('Error, not enough terms')
        return(None)
    else:
        for i in range(terms):
            if i==0:
                n=1
                q=1
                m=0
                print(n)
            else:
                m=q+n
                q=n
                n=m
                print(n)
                f_list=f_list+[n]
    print(f_list)
    return(f_list)
fibonacci(5)