from typing import List

def maxValue(self, nums: List[int]) -> List[int]:
    n = len(nums)
    if n == 0:
        return []

    prefix_max = [0] * n
    prefix_max[0] = nums[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], nums[i])

    postfix_min = [0] * n
    postfix_min[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        postfix_min[i] = min(postfix_min[i + 1], nums[i])

    ans = [0] * n
    start = 0

    for i in range(n):
        if i == n - 1 or prefix_max[i] <= postfix_min[i + 1]:
            component_max = prefix_max[i]

            for k in range(start, i + 1):
                ans[k] = component_max

            start = i + 1

    return ans
