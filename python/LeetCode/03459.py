from typing import List, Tuple
from functools import lru_cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [
            (1, 1),
            (1, -1),
            (-1, -1),
            (-1, 1),
        ]
        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def dfs(row: int, col: int, direction: int, turn: bool, target: int) -> int:
            n_row = row + DIRECTIONS[direction][0]
            n_col = col + DIRECTIONS[direction][1]
            n_target = 2 - target

            # Guard Clauses
            if not 0 <= n_row < m:
                return 0

            if not 0 <= n_col < n:
                return 0
            
            if grid[n_row][n_col] != target:
                return 0
            
            max_step = dfs(n_row, n_col, direction, turn, n_target)

            if turn:
                n_dir = (direction + 1) % 4
                max_step = max(
                    max_step,
                    dfs(n_row, n_col, n_dir, False, n_target),
                )

            return max_step + 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for direction in range(4):
                        res = max(res, dfs(i, j, direction, True, 2) + 1)
        return res
    
s = Solution()
v = s.lenOfVDiagonal([[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]])
print(v)