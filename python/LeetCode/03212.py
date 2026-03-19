from typing import List

def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])

    x_count = []
    y_count = []
    for _ in range(m):
        x_count.append([0] * n)
        y_count.append([0] * n)

    count = 0
    # Let (i, j) be equal to the bottom right corner
    for i in range(m):
        for j in range(n):
            xs = 0
            ys = 0
            if i > 0:
                xs += x_count[i - 1][j]
                ys += y_count[i - 1][j]

            if j > 0:
                xs += x_count[i][j - 1]
                ys += y_count[i][j - 1]

            if i > 0 and j > 0:
                xs -= x_count[i - 1][j - 1]
                ys -= y_count[i - 1][j - 1]

            if grid[i][j] == "X":
                xs += 1
            if grid[i][j] == "Y":
                ys += 1

            x_count[i][j] = xs
            y_count[i][j] = ys
            if xs > 0 and xs == ys:
                count += 1

    return count