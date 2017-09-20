import string
fileref=open("alice.txt",'r')
input_str=fileref.read()
input_nopunct=input_str.translate(None, string.punctuation)
input_lower=input_nopunct.lower()
input_words=input_lower.split()
glue=' '
mydict={}
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

for i in range(len(input_words)):
    if hasNumbers(input_words[i])==False:
        if input_words[i] in mydict:
            mydict[input_words[i]]=int(mydict[input_words[i]])+1 #add one to value in dict
        else:
            mydict[input_words[i]]=1    #add key to dict with value 1
keylist=list(mydict.keys())
keylist.sort()
sorteddict={}
for n in range(len(keylist)):
    sorteddict[keylist[n]]=mydict.get(keylist[n])
outputfile=open("alice_wordcount","w")
#outputfile.write(str(keylist))
for n in range(len(keylist)):
    outputfile.write(str(keylist[n])+'\t'+str(sorteddict[keylist[n]])+'\n')
#write to file
fileref.close()
outputfile.close()

#alice occurs 388 times in the book, alices 10, and alicealice once.  I see I may have differences due to how I stripped out punctuation and omitted words which contained numbers.

#the longest word in the edition I have is 'importantunimportantunimportant'.  Without the context, I don't know whether this is a scanning error that hasn't detected the spaces between the words or a deliberate style choice by Carroll.