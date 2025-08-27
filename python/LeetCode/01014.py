from typing import List

def maxScoreSightseeingPair(self, values: List[int]) -> int:
    n = len(values)
    max_overall_gain = 0
    max_end_right = values[n-1] - (n-1)
    
    for i in range(n-2, -1, -1):
        max_end_right = max(max_end_right, values[i+1] - (i+1))
        max_overall_gain = max(max_overall_gain, values[i] + i + max_end_right)
    
    return max_overall_gain