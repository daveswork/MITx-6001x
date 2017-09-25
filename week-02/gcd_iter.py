def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor = a
    while divisor > 0:
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        else:
            divisor -= 1

print(gcdIter(17,12))
