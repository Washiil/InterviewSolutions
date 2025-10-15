class Solution:
    def maxIncreasingSubarraysV1(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
            
        max_k = 0
        previous_run_length = 0
        current_run_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_run_length += 1
            else:
                # A run just ended. Update max_k based on this and the previous run.
                max_k = max(max_k, current_run_length // 2, min(current_run_length, previous_run_length))
                previous_run_length = current_run_length
                current_run_length = 1

        # Final check for the last run in the array
        max_k = max(max_k, current_run_length // 2, min(current_run_length, previous_run_length))
        
        return max_k