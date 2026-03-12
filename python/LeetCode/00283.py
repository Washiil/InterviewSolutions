from typing import List

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    non_zero = 0
    n = len(nums)
    for i in range(n):
        if nums[i] != 0:
            nums[non_zero] = nums[i]
            non_zero += 1

    for i in range(non_zero, n):
        nums[i] = 0
