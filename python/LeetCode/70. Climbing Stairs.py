def climbStairs(self, n: int) -> int:
    memo = {}
    return self.climb(n, memo)

def climb(self, n: int, memo: dict[int, int]) -> int:
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = self.climb(n - 1, memo) + self.climb(n - 2, memo)
    return memo[n]