def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    mod = 10**9 + 7

    prev = [0] * (target + 1)
    curr = [0] * (target + 1)

    prev[0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            ans = 0
            for x in range(1, k + 1):
                if j - x >= 0:
                    ans += prev[j - x] % mod
            curr[j] = ans
        prev = curr[:]
    return int(prev[target] % mod)