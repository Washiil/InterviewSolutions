def minChanges(self, s: str) -> int:
    n =  len(s)
    output = 0

    for i in range(0, n, 2):
        if s[i] != s[i + 1]:
            output += 1
    
    return output