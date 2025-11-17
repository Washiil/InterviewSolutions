from typing import List

def kLengthApart(self, nums: List[int], k: int) -> bool:
    ones = []
    for i in range(len(nums)):
        if nums[i] == 1:
            ones.append(i)
    
    if len(ones) <= 1:
        return True

    for i in range(1, len(ones)):
        if ones[i] - ones[i-1] <= k:
            return False
    

    return True