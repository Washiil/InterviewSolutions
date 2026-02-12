from collections import defaultdict

def longestBalanced(self, s: str) -> int:
    n = len(s)
    if n == 1 or n == 2:
        return n

    output = 0
    values = [ord(c) for c in s]

    for i in range(n):
        cnt = defaultdict(int)
        for j in range(i, n):
            cnt[values[j]] += 1

            unique = set(cnt.values())
            if len(unique) == 1:
                output = max(output, j - i + 1)

    return output
