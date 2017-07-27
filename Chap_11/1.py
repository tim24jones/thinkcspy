fileref=open("studentdata.txt",'r')
for aline in fileref:
    values=aline.split()
    if len(values)>7:
        print(values[0])
fileref.close()