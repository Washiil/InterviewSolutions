class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        elif len(nums) == 0:
            return 0
            
        return sum(set([x for x in nums if x > 0]))
