def rot13(input_string):
    output_string=''
    alpha='abcdefghijklmnopqrstuvwxyz'
    char_replace='nopqrstuvwxyzabcdefghijklm'
    for i in range (len(input_string)):
        for j in range (len(alpha)):
            if input_string[i].lower()==alpha[j]:
                output_string=output_string+char_replace[j]
            else:
                output_string=output_string
    return(output_string)
print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('Since rot13 is symmetric you should see this message')))
