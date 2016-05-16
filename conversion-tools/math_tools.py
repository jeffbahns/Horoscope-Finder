

def perm(n):
	n = n
	total = 1
	while n >= 1:
		total *= n
		n -= 1
	return total

def p(n, r):
	return (perm(n)) / perm(n-r)

def c(n, r):
	return (p(n,r)) / perm(r)

tot = 10


print c(48, 5)
print c(52,5)

print 1712304.0 / 2598960
