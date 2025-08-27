from typing import List

# Referenced this as my original implemntation did not meat time requirements due to being O(n^2):
# https://leetcode.com/problems/maximum-distance-in-arrays/solutions/5642927/easy-greedy-solution-beats-100/

def maxDistance(self, arrays):
    # Initalize Values
    smallest = arrays[0][0]
    biggest = arrays[0][-1]
    max_distance = 0

    for i in range(1, len(arrays)):
        arr = arrays[i]
        max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
        smallest = min(smallest, arr[0])
        biggest = max(biggest, arr[-1])

    return max_distance
