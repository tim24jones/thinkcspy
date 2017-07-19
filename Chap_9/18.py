def substCiph(message,scramb):
    alpha=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newmessage=''
    for i in range(len(message)):
        for j in range(len(scramb)):
            if message[i]==scramb[j]:
                newmessage=newmessage+alpha[j]
            else:
                    newmessage=newmessage
    print(newmessage)
    return(newmessage)
substCiph('This is the message','bcdef ghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA')