
class_dict = {}


def storeInput(name, grade):
	class_dict[name] = grade

def displayGradeList():
	print('REPORT CARD:')
	count = len(class_dict)
	gradeSum = 0
	for key, value in class_dict.iteritems():
		print(key + ' - ' + str(value))
		gradeSum = gradeSum + value
	
	print('Overall GPA - ' +str(gradeSum/count))
	
def report_card():
	num_of_classes = input('How many classes did you take? ')
	while num_of_classes != 0:
		class_name = raw_input('What was name of this class? ')
		class_grade = input('What was your grade? ')
		storeInput(class_name, class_grade)
		num_of_classes = num_of_classes -1
	displayGradeList()

	
report_card()

	

