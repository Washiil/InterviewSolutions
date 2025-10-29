def smallestNumber(self, n: int) -> int:
    v = 1
    while v < n:
        v = v * 2 + 1
    return v