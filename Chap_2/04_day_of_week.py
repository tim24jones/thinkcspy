str_init_date=input("Enter start day:")
init_date=int(str_init_date)
str_holiday_duration=input("Enter length of holiday:")
holiday_duration=int(str_holiday_duration)
return_date=(init_date+holiday_duration)%7
print("Number of day returned:",return_date)
