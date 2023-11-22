from collections import defaultdict


def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
    diags = defaultdict(list)
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            diags[i+j].append(nums[i][j])

    result = []
    for key in diags.keys():
        for value in reversed(diags[key]):
            result.append(value)
    return result
