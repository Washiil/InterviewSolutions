from typing import List

def findWords(self, words: List[str]) -> List[str]:
    row1 = "qwertyuiopQWERTYUIOP"
    row2 = "asdfghjklASDFGHJKL"
    row3 = "zxcvbnmZXCVBNM"

    output = []
    for w in words:
        valid = True
        row = -1
        if w[0] in row1:
            row = row1
        elif w[0] in row2:
            row = row2
        else:
            row = row3

        for c in w:
            if c not in row:
                valid = False
                break

        if valid:
            output.append(w)

    return output