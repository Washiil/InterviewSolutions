from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        output = 0

        for i in range(n - 1):
            odd = set()
            even = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(odd) == len(even):
                    output = max(output, j - i + 1)

        return output
