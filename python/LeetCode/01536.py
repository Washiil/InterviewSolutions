from typing import List

def minSwaps(self, grid: List[List[int]]) -> int:
    n = len(grid)

    vals = []
    for row in grid:
        last_one_idx = -1
        for i in range(n):
            if row[i] == 1:
                last_one_idx = i
        vals.append(last_one_idx)

    swaps = 0
    for i in range(n):
        target_idx = -1
        # Find the first available row that satisfies the condition
        for j in range(i, n):
            if vals[j] <= i:
                target_idx = j
                break

        if target_idx == -1:
            return -1

        swaps += (target_idx - i)

        row_val = vals.pop(target_idx)
        vals.insert(i, row_val)

    return swaps
