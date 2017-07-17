prefixes="JKLMNOPQ"
suffix="ack"
vowel_prefixes="OQ"

for p in prefixes:
    if p in vowel_prefixes:
        print(p+'u'+suffix)
    else:
        print(p+suffix)