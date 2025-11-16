def numSub(self, s: str) -> int:
    result = 0

    segments = s.split('0')
    for seg in segments:
        n = len(seg)
        result += int(n * (n + 1)/2)
    
    return result % ((10 ** 9) + 7)