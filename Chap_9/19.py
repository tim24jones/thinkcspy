def substCiph(message,scramb):
    alpha=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newmessage=''
    for i in range(len(message)):
        for j in range(len(alpha)):
            if message[i]==alpha[j]:
                newmessage=newmessage+scramb[j]
            else:
                    newmessage=newmessage
    print(newmessage)
    return(newmessage)
substCiph('Sghrehresgcelcrrzfc','bcdef ghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA')