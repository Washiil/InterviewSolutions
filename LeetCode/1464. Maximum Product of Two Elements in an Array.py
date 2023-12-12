def maxProduct(self, nums: list[int]) -> int:
    nums = sorted(nums)
    x = (nums[-1] - 1) * (nums[-2] - 1)
    return x
