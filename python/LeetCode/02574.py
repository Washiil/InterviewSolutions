def leftRightDifference(self, nums: list[int]) -> list[int]:
    right_sum = sum(nums)
    n = len(nums)

    left_sum = 0
    result = [0] * len(nums)

    for i in range(n):
        right_sum -= nums[i]
        result[i] = (abs(left_sum - right_sum))
        left_sum += nums[i]

    return result
