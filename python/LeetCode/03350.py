from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        run_lengths = []
        current_length = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                current_length += 1
            else:
                run_lengths.append(current_length)
                current_length = 1
        run_lengths.append(current_length) # Add the last run

        max_k = 0
        
        for length in run_lengths:
            max_k = max(max_k, length // 2)
            
        for i in range(len(run_lengths) - 1):
            k_from_adjacent = min(run_lengths[i], run_lengths[i+1])
            max_k = max(max_k, k_from_adjacent)
            
        return max_k