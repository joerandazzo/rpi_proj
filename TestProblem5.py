
def computePoly(num, coeff):
	val = 0
	for i, item in enumerate(coeff):
		val= val+ item*num**i
		print(val)
	return val


number = 9
coeffecients = [6,5,4,3,2,1]

summation = computePoly(number, coeffecients)
print(summation)
