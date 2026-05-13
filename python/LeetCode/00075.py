from typing import List

def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    r, w, b = 0, 0, 0

    for colour in nums:
        if colour == 0:
            r += 1
        elif colour == 1:
            w += 1
        elif colour == 2:
            b += 1
        else:
            raise ValueError()

    nums[:] = [0]*r + [1]*w + [2]*b

    return nums
