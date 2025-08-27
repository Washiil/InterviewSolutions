from typing import List

def longestSubarray(self, nums: List[int]) -> int:
    maximum_val = max(nums)

    output = 0
    current_streak = 0
    
    for num in nums:
        if num == maximum_val:
            current_streak += 1  # Increment the streak of 5's
        elif current_streak > 0:
            output = max(output, current_streak)
            current_streak = 0  # Reset streak
    
    # Handle the case where the array ends with a sequence of 5's
    output = max(output, current_streak)
    
    return output