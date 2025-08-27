def numJewelsInStones(self, jewels: str, stones: str) -> int:
    return sum([stones.count(j) for j in jewels])