def halvesAreAlike(self, s: str) -> bool:
    l = len(s) // 2
    first = s[:l]
    last = s[l:]

    return len([char for char in first if char in "aeiouAEIOU"]) == len([char for char in last if char in "aeiouAEIOU"])