def minPairSum(self, nums: List[int]) -> int:
    nums.sort()
    big = float('-inf')
    l = len(nums)
    for i in range(l // 2):
        x = nums[i] + nums[l - i - 1]
        if x > big:
            big = x

    return big
