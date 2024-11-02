def isCircularSentence(self, sentence: str) -> bool:
    cstart = sentence[0]
    cend = sentence[-1]

    if cstart != cend:
        return False

    words = sentence.split(' ')
    for i in range(len(words) - 1):
        if words[i][-1] != words[i + 1][0]:
            return False
    
    return True