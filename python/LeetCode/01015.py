def smallestRepunitDivByK(self, k: int) -> int:
    '''
    Find some integer n consisting of only 1's where n % k == 0

    n may not fit in a 64-bit signed integer.

    Bit Manipulation, modulus
    1111111
    '''
    # number divisible by 2 or 5 cannot end in 1 
    if k % 2 == 0 or k % 5 == 0:
        return -1
    
    rem = 0
    for l in range(1, k + 1):
        rem = (rem * 10 + 1) % k
        if rem == 0:
            return l
    
    return -1