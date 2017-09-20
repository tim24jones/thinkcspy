fileref=open("The Project Gutenberg Etext of Alice's Adventures in Wonderland, by Lewis Carroll",'r')
input_lower=fileref.lower()
input_words=input_lower.split()
glue=' '
dict={}
for i in range(len(input_words)):
    if input_words[i] in dict
        dict(inputwords[i])=int(dict(inputwords[i]))+1 #add one to value in dict
    else:
        dict(inputwords[i]=1    #add key to dict with value 1
keylist=list(dict.keys())
keylist.sort()
outputfile=open("alice_wordcount","w")
outputfile.write
for k in keylistfulldict:
    outputfile.write(k,'\t',dict[k] '\n')
#write to file
fileref.close()
outputfile.close()
