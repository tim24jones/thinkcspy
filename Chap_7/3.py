def getGrade(grade):
	if (grade<60):
        	return 'F'
	elif (grade>=60 and grade<70):
		return 'D'
	elif (grade>=70 and grade<80):
		return 'C'
	elif (grade>=80 and grade<90):
		return 'B'
	elif (grade>=90):
		return 'A'
	else:
		return 'Error'
getGrade(67)