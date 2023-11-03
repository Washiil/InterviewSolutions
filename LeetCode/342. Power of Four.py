from math import log


def isPowerOfFour(self, n: int) -> bool:
    if n == 1:
        return True
    if n <= 0:
        return False

    log4 = log(n, 4)
    return (log4 == int(log4))
