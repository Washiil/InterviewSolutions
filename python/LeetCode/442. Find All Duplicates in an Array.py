from typing import List

def findDuplicates(self, nums: List[int]) -> List[int]:
    x = [0] * (len(nums) + 1)
    result = []

    for i in nums:
        if x[i] == 1:
            result.append(i)
        else:
            x[i] = 1

    return result
