from typing import List

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    counts = {}
    output = []

    for x in nums1:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    for x in nums2:
        if x in counts and counts[x] > 0:
            counts[x] -= 1
            output.append(x)

    return output
