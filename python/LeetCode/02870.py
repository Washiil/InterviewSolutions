def minOperations(self, nums: list[int]) -> int:
    counts = {}
    total = 0

    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    for val in counts.values():
        x = val
        while x > 4:
            x -= 3
            total += 1
        
        if x == 3:
            x -= 3
            total += 1
        
        while x >= 2:
            x -= 2
            total += 1
        
        if x != 0:
            return -1
    
    return total