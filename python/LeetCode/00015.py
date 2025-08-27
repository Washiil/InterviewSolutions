from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
    output = []
    nums.sort()
    length = len(nums)

    for fixed in range(length):
        if fixed > 0 and nums[fixed] == nums[fixed - 1]:
            continue
        
        left = fixed + 1
        right = length - 1

        while left < right:
            total = nums[fixed] + nums[left] + nums[right]

            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                output.append([nums[fixed], nums[left], nums[right]])
                left += 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    
    return output
