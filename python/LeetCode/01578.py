from typing import List

def minCost(self, colors: str, neededTime: List[int]) -> int:
    '''
    Assumptions:
        colors[i] is the color of the ith balloon.
        - colors contains only lowercase English letters.
        colourful: two consecutive balloons to be of the same color

        neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
        - 1 <= neededTime[i] <= 104

        Return the minimum time Bob needs to make the rope colorful.
    
    Idea:
        Whenever there is a grouping of 2 or more adjacent same coloured ballons pick the minimum of that subarray
        O(n)
    '''
    n = len(colors)
    output = 0

    l = 0
    r = 0
    prev_col = colors[l]
    while r < n:
        if colors[r] != prev_col:
            num_to_remove = (r - l) - 1

            s = sorted(neededTime[l:r])
            output += sum(s[:num_to_remove])

            prev_col = colors[r]
            l = r

        r += 1
    
    num_to_remove = (r - l) - 1
    s = sorted(neededTime[l:r])
    output += sum(s[:num_to_remove])
    
    return output
