from math import floor

def concatenatedBinary(self, n: int) -> int:
    MOD = 1_000_000_007

    tmp = ''
    for i in range(1, n + 1):
        tmp += bin(i)[2:]

    total = int(tmp, 2) % MOD

    return floor(total)