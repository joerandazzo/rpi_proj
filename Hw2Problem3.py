#Homework 2, Problem 3
#Joe Randazzo

success = [50,51,52,53,54,55]

for i in range(10):
	for j in range(10):
		for k in range(10):
			n=(6*i)+(9*j)+(20*k)
			
			for val in success:
				if n == val:
					print ('Success at 6*' + str(i) + '+9*' 
					+str(j) + '+20*' + str(k) + '='+ str(n))
					
			
			
