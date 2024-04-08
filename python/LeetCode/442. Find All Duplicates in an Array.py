from typing import List

def findDuplicates(self, nums: List[int]) -> List[int]:
    x = [0] * (len(nums) + 1)
    result = []

    for i in nums:
        if x[i] == 1:
            result.append(i)
        else:
            x[i] = 1
<<<<<<< HEAD
    
    return result
=======

    return result
>>>>>>> 5baeb8ae39ab8d2de8e092ce9d4c4dadb1c6e5e3
