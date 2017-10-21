input_str=str(input("Please enter a sentence:"))
input_lower=input_str.lower()
input_words=input_lower.split()
glue=' '
pirate_dict={'sir':'matey','hotel':'fleabag inn','student':'swabbie','boy':'matey','madam':'lassie','professor':'foul blaggart','restaurant':'galley','your':'yer','excuse':'arr','students':'swabbies','are':'be','lawyer':'foul blaggart','the':"th'",'restroom':'head','my':'me','hello':'avast','is':'be','man':'matey'}
for i in range(len(input_words)):
    if input_words[i] in pirate_dict:
        input_words[i]=pirate_dict[input_words[i]]
newstring=glue.join(input_words)
print(newstring)
