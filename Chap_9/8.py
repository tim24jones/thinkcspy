def remove_letter(theLetter, theString):
    vowels = "aeiouAEIOU"
    sWithoutLetter = ""
    for eachChar in theString:
        if eachChar not in theLetter:
            sWithoutLetter = sWithoutLetter + eachChar
    return sWithoutLetter

print(remove_letter('p',"compsci"))
print(remove_letter('e',"aAbEefIijOopUus"))