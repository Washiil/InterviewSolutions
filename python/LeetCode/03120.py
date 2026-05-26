def numberOfSpecialChars(self, word: str) -> int:
    count = 0
    seen = set()

    for c in word:
        idx = ord(c)

        if idx in seen:
            continue

        seen.add(idx)
        if idx + 32 in seen or idx - 32 in seen:
            count += 1

    return count
