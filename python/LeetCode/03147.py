def maximumEnergy(self, energy: List[int], k: int) -> int:
    n = len(energy)
    dp = [0 for _ in range(n)]

    for start in range(n-1, -1, -1):
        if start + k > n-1:
            dp[start] = energy[start]
        else:
            dp[start] = energy[start] + dp[start + k]
    
    return max(dp)