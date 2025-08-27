def maximumUniqueSubarray(self, nums: List[int]) -> int:
    left = 0
    seen = set()

    current_score = 0
    max_score = 0

    for right in range(len(nums)):
        num = nums[right]

        while num in seen:
            current_score -= nums[left]
            seen.remove(nums[left])
            left += 1
        
        current_score += num
        seen.add(num)
        
        max_score = max(max_score, current_score)
        
    return max_score
