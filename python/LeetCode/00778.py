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

        mins = []
        for i in range(1, n-1):
            mins.append(min(grid[i]))
            mins.append(min([grid[i][j] for j in range(n)]))
        
        if len(mins) > 0:
            t += max(mins)
        

        while True:
            visited = [[0 for _ in range(n)] for _ in range(n)]
            if self.dfs(0, 0, grid, visited, t):
                return t

            t += 1

        return -1