from typing import List

def isOneBitCharacter(self, bits: List[int]) -> bool:
    n = len(bits)
    i = 0

    while i < n - 1:
        if bits[i] == 1:
            i += 2 # Skipping 10 or 11
        else:
            i += 1 # 0
        
    return i == n - 1
    
