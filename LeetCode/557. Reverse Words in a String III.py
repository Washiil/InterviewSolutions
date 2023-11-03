class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        rev_words = []
        for x in words:
            rev_words.append(x[::-1])

        return ' '.join(rev_words)
