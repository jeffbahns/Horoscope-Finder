# Fibonacci Sequence

# returns Fibonacci Sequence to nth digit

def fibonacci(counter):
    a, b, c = 0, 1, 0
    print (0)
    for i in range(0,counter-1):
        c = a + b
        a = b
        b = c
        print (c)
    return None

