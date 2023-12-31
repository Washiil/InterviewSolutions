def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    l = len(s)
    longest = -1

    for i in range(l):
        c1 = s[i]
        for j in range(l - 1, i, -1):
            if (j - i - 1) <= longest:
                break
            if s[j] == c1:
                longest = j - i - 1
                break


    return longest