from typing import List

def lemonadeChange(self, bills: List[int]) -> bool:
    fives = 0
    tens = 0

    for b in bills:
        if b == 5:
            fives += 1
        elif b == 10:
            if fives > 0:
                fives -= 1
                tens += 1
            else:
                return False
        else:
            if tens > 0 and fives > 0:
                fives -= 1
                tens -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    
    return True