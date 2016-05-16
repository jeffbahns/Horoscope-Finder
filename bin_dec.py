# Binary/Decimal Converter

def bin_2_dec(n):
    global binstr
    remainder = n // 2
    while n > 1:
        return bin_2_dec(remainder) + [n % 2]

