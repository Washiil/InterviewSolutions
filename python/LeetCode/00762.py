from math import ceil, sqrt

def is_prime(self, n):
    if n < 2:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, ceil(sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve[n]

def countPrimeSetBits(self, left: int, right: int) -> int:
    count = 0

    for i in range(left, right + 1):
        if self.is_prime(bin(i).count("1")):
            count += 1
    return count
