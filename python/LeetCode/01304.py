def sumZero(self, n: int) -> List[int]:
    arr = []
    if n % 2 == 0:
        for i in range(1, (n // 2) + 1):
            arr.append(i)
            arr.append(i * -1)
    else:
        arr.append(0)
        for i in range(1, (n // 2) + 1):
            arr.append(i)
            arr.append(i * -1)
    
    return arr
