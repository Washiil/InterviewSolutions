from typing import List

def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
    max_area = 0
    max_diag = 0

    for l, w in dimensions:
        curr_diag = l * l + w * w
        area = l * w

        if curr_diag > max_diag:
            max_diag = curr_diag
            max_area = area
        elif curr_diag == max_diag:
            max_area = max(area, max_area)

    return max_area
