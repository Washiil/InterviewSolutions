def climb(n):
    result = []
    while n >= 1:
        result.append(n)
        n = n // 2
    
    return list(reversed(result))