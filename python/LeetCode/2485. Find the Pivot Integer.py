def pivotInteger(self, n: int) -> int:
    pre = 0
    post = 0

    x = 1
    while pre <= post:
        pre = sum([n for n in range(1, x + 1)])
        post = sum([n for n in range(x, n + 1)])
        if pre == post:
            return x
        else:
            x += 1
    return -1