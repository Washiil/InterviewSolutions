def rob(self, nums: list[int]) -> int:
    p1 = 0
    p2 = 0
    for i in nums:
        p2, p1 = p1, max(p1, p2 + i)
    return p1