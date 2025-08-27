from typing import List

def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    consec = 0
    for x in arr:
        if x % 2 == 0:
            consec = 0
            continue

        consec += 1
        if consec == 3:
            return True
    
    return False