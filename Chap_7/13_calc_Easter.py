year=int(input("What year is it?"))
if (year<=1900):
    print('Date too small')
elif (year>=2099):
    print('Date too large')
elif year in [1954,1981,2049,2076]:
    f=7
else:
    f=0
a=year%19
b=year%4
c=year%7
d=(19*a+24)%30
e=(2*b+4*c+6*d+5)%7
dateofeaster=22+d+e-f
print(dateofeaster)
