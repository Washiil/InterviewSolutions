from collections import defaultdict


def countNicePairs(self, nums: list[int]) -> int:
    res = 0
    d = defaultdict(int)
    for n in nums:
        k = n - int(str(n)[::-1])
        res += d[k]
        d[k] += 1
    return res % (10**9 + 7)
