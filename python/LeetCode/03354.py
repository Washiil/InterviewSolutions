def countValidSelections(self, nums: List[int]) -> int:
    n = len(nums)
    dx = -1
    total = 0 
    for i, v in enumerate(nums):
        if v == 0:
            left_sum = sum(nums[0:i])
            right_sum = sum(nums[i:n])
            diff = abs(left_sum - right_sum)

            print(left_sum, right_sum)

            if diff == 0:
                total += 2
            elif diff == 1:
                total += 1 

    return total
