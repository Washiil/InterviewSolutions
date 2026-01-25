from typing import List

def minimumDifference(self, nums: List[int], k: int) -> int:
    nums.sort()
    n = len(nums)

    min_diff = float('inf')
    for i in range(n - k + 1):
        total = nums[i + k - 1] - nums[i]
        min_diff = min(total, min_diff)

    return min_diff
