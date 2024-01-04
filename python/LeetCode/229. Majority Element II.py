def majorityElement(self, nums: list[int]) -> list[int]:
    m = len(nums) // 3
    values = {}
    for i in nums:
        values[i] = values.get(i, 0) + 1

    return [x for x in values if values[x] > m]
