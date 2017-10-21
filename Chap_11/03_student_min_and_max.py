fileref=open("studentdata.txt",'r')
print('NAME', '\t', 'Max', '\t', 'Min')
for aline in fileref:
    values=aline.split()
    maxline=values[1]#initializing
    minline=values[1]
    for i in range(1,len(values)):
        if values[i]<minline:
            minline=values[i]
        if values[i]>maxline:
            maxline=values[i]
    print(values[0],'\t', maxline, '\t', minline)
fileref.close()
