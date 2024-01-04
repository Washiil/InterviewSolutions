from collections import defaultdict 

def makeEqual(self, words: list[str]) -> bool:
    chars = defaultdict(lambda: 0)

    for word in words:
        for c in word:
            chars[c] += 1
    
    for i in chars.values():
        if i % len(words) != 0:
            return False
    
    return True