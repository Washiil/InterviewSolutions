from typing import List

def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    distance = 0
    n = len(points)

    for i in range(1, n):
        prev_x, prev_y = points[i - 1]
        new_x, new_y = points[i]

        dx, dy = abs(prev_x - new_x), abs(prev_y - new_y)

        diag = min(dx, dy)
        distance += diag + (dx - diag) + (dy - diag)

    return distance
