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

        if self.dfs(r + 1, c, grid, visited, t):
            return True
        if self.dfs(r - 1, c, grid, visited, t):
            return True
        if self.dfs(r, c + 1, grid, visited, t):
            return True
        if self.dfs(r, c - 1, grid, visited, t):
            return True

        visited[r][c] = 0

        return False


    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        lower = grid[0][0]
        upper = n * n - 1
        ans = upper

        while lower <= upper:
            mid = (lower + upper) // 2
            visited = [[0 for _ in range(n)] for _ in range(n)]

            if self.dfs(0, 0, grid, visited, mid):
                ans = mid
                upper = mid - 1
            else:
                lower = mid + 1

        return ans