# binconv.py
# contains different tools for converting to and from decimal, binary, hex, and octal number systems
# left unfinished because i only needed certain functions for a homework assignment

## base 10 -> base 2 converter
def dec2bin(num):
	num = num
	binaryString = ""
	if num > 0:
		binaryString += str(dec2bin(num // 2)) + str(num % 2)
	return binaryString

def dec2oct(num):
	pass

def dec2hex(num):
	pass

#############


## base 2 -> base 10 converter
def bin2dec(num):
	binaryString = str(num)[::-1]
	decimalTotal = 0
	exponent = len(binaryString)-1
	while exponent >= 0:
		decimalTotal += (int(binaryString[exponent])) * (2 ** exponent)
		exponent -= 1
	return decimalTotal

def bin2hex(num):
	pass

def bin2oct(num):
	pass

#############


## base 8 -> base 10 converter
def oct2dec(num):
	octalString = str(num)[::-1]
	decimalTotal = 0
	exponent = len(octalString)-1
	while exponent >= 0:
		decimalTotal += (int(octalString[exponent])) * (8 ** exponent)
		exponent -= 1
	return decimalTotal

def oct2bin(num):
	return dec2bin(oct2dec(inp))

def oct2hex(num):
	pass

#############

## base 16 -> base 10, base 2, base 8 systems
def hex2dec(num):
	hexDict = {	'0' : 0, '1' : 1, '2' : 2, '3' : 3,
				'4' : 4, '5' : 5, '6' : 6, '7' : 7,
				'8' : 8, '9' : 9, 'A' : 10,'B' : 11,
				'C' : 12,'D' : 13,'E' : 14,'F' : 15 }
	hexString = str(num)[::-1]
	decimalTotal = 0
	exponent = len(hexString) - 1
	while exponent >= 0:
		decimalTotal += (hexDict[hexString[exponent]]) * (16 ** exponent)
		exponent -= 1
	return decimalTotal



def hex2bin(num):	
	pass
def hex2oct(num):
	pass

#############


inp = 4532
inp2 = "1AE"
print(dec2bin(inp))

