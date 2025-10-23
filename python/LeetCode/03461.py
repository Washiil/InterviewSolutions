def hasSameDigits(self, s: str) -> bool:
    lst = [int(v) for v in s]
    while len(lst) != 2:
        nums = [int(v) for v in lst]
        out = []
        for i in range(0, len(lst)-1):
            out.append((nums[i] + nums[i+1]) % 10)
        
        lst = out
    
    if lst[0] == lst[1]:
        return True
    return False