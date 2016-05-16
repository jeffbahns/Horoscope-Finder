# CC Number Validator

def ccvalidator(ccn):
    ccn = [int(i) for i in str(ccn)]
    i = 1
    ccs = ""
    total = 0
    for digit in ccn:
        if i % 2 == 0:
            ccs += str(digit)
            i += 1
        else:
            ccs += str(digit*2)
            i += 1
    for digit in ccs:
        total += int(digit)
    return total % 2 == 0

#print (ccvalidator( xxxx - xxxx - xxxx - xxxx))
