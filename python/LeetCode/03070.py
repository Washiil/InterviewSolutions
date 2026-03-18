from typing import List

def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
    m = len(grid)
    n = len(grid[0])

    mat = [[0] * n for _ in range(m)]

    output = 0
    # Let (i, j) be the bottom right corner
    for i in range(m):
        for j in range(n):
            tmp = 0
            if i > 0:
                tmp += mat[i - 1][j]
            if j > 0:
                tmp += mat[i][j - 1]
            tmp += grid[i][j]

            if i > 0 and j > 0:
                tmp -= mat[i - 1][j - 1]
            mat[i][j] = tmp
            if tmp <= k:
                output += 1

    return output
