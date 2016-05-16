# Very simple function used to check my solutions
# on a discrete math assignment

def modTool(dividend, divisor):
	quotient = dividend // divisor
	remainder = dividend % divisor
	result = "{} = {} x {} + {}".format(str(dividend), str(divisor), str(quotient), str(remainder))
	return result


questionDict = {-45 : 24}

for dividend in questionDict:
	print(modTool(dividend, questionDict[dividend]))
	print("\n\n\n\n\n\n________________________")

