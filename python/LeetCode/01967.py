def numOfStrings(self, patterns: list[str], word: str) -> int:
    count = 0
    for pat in patterns:
        if pat in word:
            count += 1
    return count
