def palindrome(self, word) -> bool:
    i, j = 0, len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

def firstPalindrome(self, words: List[str]) -> str:
    for pal in words:
        if self.palindrome(pal):
            return pal
    return ""