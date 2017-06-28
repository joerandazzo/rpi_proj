#Day 6 Assignments
#Joe Randazzo


##Assignment 3
N = input("Please enter a number as an upper limit:")
N = int(N)

for i in range(2, N):
	check_var = True
	for k in range(2,i):
		if(i%k) == 0:
			check_var = False
	if check_var:
		print(i)
		
		
print("\n Assignment 3 Functionality: The code accepts number input. The for loop will iterate based off the input. \
 There is one loop with a nested loop. The nested loop will check the remainder between the two values and see if\
 they equal zero. After the nested loop finishes, it will print if no zero remainders are found.")


