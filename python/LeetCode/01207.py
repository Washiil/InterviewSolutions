def uniqueOccurrences(self, arr: list[int]) -> bool:
    count = {}
    for val in arr:
        count[val] = count.get(val, 0) + 1

    if len(set(count.values())) == len(count.values()):
        return True
    return False
