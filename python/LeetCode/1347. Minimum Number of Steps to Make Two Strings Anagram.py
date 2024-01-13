def minSteps(self, s: str, t: str) -> int:
    count = [0] * 26

    for c in s:
        count[ord(c) - 97] += 1
    
    for c in t:
        count[ord(c) - 97] -= 1
    
    x = sum(map(abs, count))
    return x // 2