from typing import List

def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])

    ans = [([0] * (n - k + 1)) for _ in range(m - k + 1)]

    # Consider (row, col) to be the start (top left corner) of a submatrix
    for row in range(m):
        for col in range(n):
            unique_values = set()

            if row + k > m or col + k > n:
                break

            for r in range(k):
                for c in range(k):
                    unique_values.add(grid[row + r][col + c])

            unique_values = sorted(list(unique_values))

            if len(unique_values) < 2:
                break

            min_abs_diff = abs(unique_values[0] - unique_values[1])
            for v1, v2 in zip(unique_values, unique_values[1:]):
                min_abs_diff = min(min_abs_diff, abs(v1 - v2))

            ans[row][col] = min_abs_diff

    return ans