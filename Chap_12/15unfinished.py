input_str=input("Please enter a sentence:")
lower_str=input_str.lower()
mydict={}
for i in range(len(lower_str)):
    char=lower_str[i]
    if char not in mydict:
        mydict[char]=1
    else:
        mydict[char]=mydict[char]+1
    print(char,'\t',mydict[char])
