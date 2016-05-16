
# Factor Finder

def factorfind(num):
	factors = []
	for i in range(1, num+1):
		if num % i == 0:
			factors.append(i)
	return factors
print (factorfind(1529))
print (factorfind(14039))