class Solution:
    def maxIncreasingSubarraysV2(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        inc_from_left = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_from_left[i] = inc_from_left[i-1] + 1
        
        inc_from_right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                inc_from_right[i] = inc_from_right[i+1] + 1
        
        max_k = 0
        for i in range(n - 1):
            k_from_adjacent = min(inc_from_left[i], inc_from_right[i+1])
            max_k = max(max_k, k_from_adjacent)

        for length in inc_from_left:
             max_k = max(max_k, length // 2)

        return max_k