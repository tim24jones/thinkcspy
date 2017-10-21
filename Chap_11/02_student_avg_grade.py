fileref=open("studentdata.txt",'r')
for aline in fileref:
    values=aline.split()
    sumvalues=0
    for i in range(1,len(values)):
        sumvalues=sumvalues+int(values[i])
    average=sumvalues/(len(values)-1)
    print(values[0],'\t', average)
fileref.close()
