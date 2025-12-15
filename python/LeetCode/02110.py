from typing import List
from math import floor

def getDescentPeriods(self, prices: List[int]) -> int:
    n = len(prices)
    streak = 1
    output = 0

    for i in range(n-1):
        diff = prices[i] - prices[i + 1]
        if diff != 1:
            output += (((streak) *  (streak+1)) / 2) - streak
            streak = 1
        else:
            streak += 1
    
    output += (((streak) *  (streak+1)) / 2) - streak
    
    print(output, n)
    return floor(output + n)
        