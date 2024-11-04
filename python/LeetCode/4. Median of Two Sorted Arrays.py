from typing import List
import math

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    s = sorted(nums1 + nums2)
    n = len(s)

    if n % 2 == 1:
        return s[int(n / 2)]
    else:
        base_index = int(n / 2)
        return (s[base_index] + s[base_index - 1]) / 2