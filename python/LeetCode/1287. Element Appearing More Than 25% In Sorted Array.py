def findSpecialInteger(self, arr: list[int]) -> int:
    x = set(arr)
    l = len(arr)
    for val in x:
        if arr.count(val) > l * 0.25:
            return val

    return 0
