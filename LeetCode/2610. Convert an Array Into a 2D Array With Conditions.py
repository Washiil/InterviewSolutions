def filter_nums(self, nums) -> (list[int], list[int]):
    unique = []
    dups = []
    for num in nums:
        if num not in unique:
            unique.append(num)
        else:
            dups.append(num)
    
    return (unique, dups)


def findMatrix(self, nums: list[int]) -> list[list[int]]:
    rows = []

    while nums:
        x, y = self.filter_nums(nums)
        nums = y
        rows.append(x)
    
    return rows