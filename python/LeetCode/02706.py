def buyChoco(self, prices: list[int], money: int) -> int:
    cheap = sorted(prices)
    leftover = money - cheap[0] - cheap[1]
    return leftover if leftover >= 0 else money
