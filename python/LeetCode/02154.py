from typing import List

def findFinalValue(self, nums: List[int], original: int) -> int:
    '''
    Assumptions:
    `original` is the first number that needs to be searched for in nums.
    
    Steps:
    1. If original is found in nums, set original = 2 * original.
    2. Otherwise, stop the process.
    3. Repeat this process with the new number as long as you keep finding the number.

    Returns: the final value of original.

    Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i], original <= 1000
    '''

    while original in nums:
        original = original * 2
    
    return original