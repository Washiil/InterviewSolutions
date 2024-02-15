def largestPerimeter(self, nums: list[int]) -> int:
    sides = sorted(nums)
    prev_sum = 0
    res = -1
    for num in sides:
        if num < prev_sum:
            res = num + prev_sum
        prev_sum += num
    return res