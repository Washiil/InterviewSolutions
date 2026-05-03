def rotateString(self, s: str, goal: str) -> bool:
    n = len(s)
    for i in range(n):
        if s[n - (n - i):] + s[:i] == goal:
            return True

    return False
