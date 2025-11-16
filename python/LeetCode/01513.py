def numSub(self, s: str) -> int:
    result = 0
    count = 0

    for c in s:
        if c == '1':
            count += 1
            result = (result + count) % ((10 ** 9) + 7)
        else:
            count = 0
    
    return result