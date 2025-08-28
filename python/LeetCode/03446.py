from typing import List

def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)

    # Top right
    for col in range(1, n):
        tmp = []
        for row in range(n - col):
            tmp.append(grid[row][col + row])
        
        tmp.sort()
        idx = 0
        for row in range(n - col):
            grid[row][col + row] = tmp[idx]
            idx += 1


    # Bottom left
    for row in range(n):
        tmp = []
        for col in range(n - row):
            tmp.append(grid[row + col][col])
        
        tmp.sort(reverse=True)
        idx = 0
        for col in range(n - row):
            grid[row + col][col] = tmp[idx]
            idx += 1
    
    return grid