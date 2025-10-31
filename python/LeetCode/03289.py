from typing import List

def getSneakyNumbers(self, nums: List[int]) -> List[int]:
    n = len(nums)
    seen = set()

    output = []
    for i in nums:
        if i in seen:
            output.append(i)
            if len(output) == 2:
                return output
        seen.add(i)