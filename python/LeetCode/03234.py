def numberOfSubstrings(self, s: str) -> int:
    # str dominant ones if (1 count) >= (0 count)^2.

    n = len(s)
    l = 0
    r = 0

    count_1 = 0
    count_0 = 0

    dominant = 0
    
    while l < n:
        count_1 = 0
        count_0 = 0
        while r < n:
            # Handle Counters
            if s[r] == '0':
                count_0 += 1
            else:
                count_1 += 1

            # early exit if dominate 1 not possible in remaining subtstring
            if (count_0 ** 2) > n:
                break

            if count_1 >= (count_0) ** 2:
                dominant += 1
            
            r += 1
        
        l += 1
        r = l
    
    return dominant
        
