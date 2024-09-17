from typing import List

def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    words = {}
    output = []

    for word in s1.split(' '):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    for word in s2.split(' '):
        if word in words:
            words[word] = 0
        else:
            words[word] = 1
    
    for k, v in words.items():
        if v == 1:
            output.append(k)
    
    return output