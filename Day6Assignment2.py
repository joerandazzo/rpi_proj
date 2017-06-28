#Day 6 Assignments
#Joe Randazzo
#Assignment 2
hours = input("Number of hours worked this week? ")
rate = input('What is your rate? ')

if hours>40:
	rate = rate * 1.5
	
pay = hours * rate
print('Here is your paycheck! ' + str(pay))
ß
##Assignment 3
print("\n Assignment 3 Functionality: The code accepts number input. The for loop will iterate based off the input. \
 There is one loop with a nested loop. The nested loop will check the remainder between the two values and see if\
 they equal zero. After the nested loop finishes, it will print if no zero remainders are found.")

