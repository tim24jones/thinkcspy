input_str=input("Please enter a sentence:")
lower_str=input_str.lower
mydict={lower_str[0]:1}#error here, does not support indexing
for i in range(1,len(lower_str)):
    if lower_str[i] not in mydict:
        mydict=mydict+{char:1}
    else:
        mydict[char]=mydict[char]+1