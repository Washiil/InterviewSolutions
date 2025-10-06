class Solution:
    def dfs(self, r, c, grid, visited, t) -> bool:
        n = len(grid)
        # Bounds checks
        if not (0 <= r < n and 0 <= c < n):
            return False
        # Height and visited check
        if grid[r][c] > t or visited[r][c]:
            return False
        # Base case for success
        if r == n-1 and c == n-1:
            return True

        visited[r][c] = 1

        # Explore all four directions
        if self.dfs(r + 1, c, grid, visited, t):
            return True
        if self.dfs(r - 1, c, grid, visited, t):
            return True
        if self.dfs(r, c + 1, grid, visited, t):
            return True
        if self.dfs(r, c - 1, grid, visited, t):
            return True

        # Backtracking: un-mark the cell if no path was found from this point
        visited[r][c] = 0

        return False


    def swimInWater(self, grid: List[List[int]]) -> int:
        t = 0
        n = len(grid)

        lower, upper = 0, 0, 0

        for i in range(n):
            for j in range(n):
                lower = min(lower, grid[i][j])
                upper = max(upper, grid[i][j])

        mins = []
        for i in range(1, n-1):
            mins.append(min(grid[i]))
            mins.append(min([grid[i][j] for j in range(n)]))
        
        if len(mins) > 0:
            t += max(mins)
        
        while lower < upper:
            mid = (lower + upper) // 2
            visited = [[0 for _ in range(n)] for _ in range(n)]
            if self.dfs(0, 0, grid, visited, t):
                t = mid
                upper = mid-1
            else:
                lower = mid+1

        return t