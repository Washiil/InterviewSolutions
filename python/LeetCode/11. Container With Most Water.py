from typing import List

def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1

    maximum = 0

    while left < right:
        volume = (right - left) * min(height[left], height[right])
        maximum = max(volume, maximum)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return maximum