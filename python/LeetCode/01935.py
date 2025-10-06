def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    output = 0
    for word in text.split(' '):
        valid = True

        for c in word:
            if c in brokenLetters:
                valid = False
                break

        if valid:
            output += 1
    
    return output
