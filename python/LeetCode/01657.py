'''
Shoutout https://leetcode.com/MarkSPhilip31/ for the answer, still unsure how mine is incorrect
def closeStrings(self, word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    
    x = set(word1)
    y = set(word2)

    z = x.union(y)

    return len(z) > 0
'''

def closeStrings(self, word1: str, word2: str) -> bool:
    freq1 = [0] * 26
    freq2 = [0] * 26

    for ch in word1:
        freq1[ord(ch) - ord('a')] += 1

    for ch in word2:
        freq2[ord(ch) - ord('a')] += 1

    for i in range(26):
        if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
            return False

    freq1.sort()
    freq2.sort()

    for i in range(26):
        if freq1[i] != freq2[i]:
            return False

    return True

