str_init_time=input("Enter initial time on clock:")
init_time=int(str_init_time)
str_alarm_duration=input("Time until the alarm:")
alarm_duration=int(str_alarm_duration)
alarm_time=(init_time+alarm_duration)%24
print("Time of alarm:",alarm_time)