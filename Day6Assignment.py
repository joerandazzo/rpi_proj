#Day 6

#Asignment 1
##name = raw_input("What is your name? ")
##print('Welcome '+ name)

#Assignment 2
hours = input("Number of hours worked this week? ")
rate = input('What is your rate? ')

if hours>40:
	rate = rate * 1.5
	
pay = hours * rate
print('Here is your paycheck! ' + str(pay))
