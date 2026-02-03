from typing import List

def isTrionic(self, nums: List[int]) -> bool:
    n = len(nums)

    if nums[1] - nums[0] < 0:
        return False

    curr_direction = False
    count = 0
    for i in range(n - 1):
        v1 = nums[i]
        v2 = nums[i + 1]

        if v2 - v1 == 0:
            return False

        direction = v2 - v1 > 0
        if direction != curr_direction:
            count += 1
            curr_direction = direction

        if count > 3:
            return False

    return count == 3