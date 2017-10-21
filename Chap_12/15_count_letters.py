def count(p,letter):
    letter=str(letter)
    a=0
    t=0
    for i in range (len(p)):
        if p[i]==letter:
            a=a+1
            t=t+1
        else:
            t=t+1
    dict={letter:a}
    return(dict)

def main():
    input_str=str(input("Please enter a sentence:"))
    print("Please enter a sentence:", input_str)
    alphastr='. abcdefghijklmnopqrstuvwxyz1234567890'
    newstr=input_str.lower()
    for i in range(len(alphastr)):
        fulldict={}
        fulldict=fulldict.items()+count(newstr,alphastr[i]).items()
        for k,v in fulldict:
            if v!=0:
                print(k,'\t',v)
main()
