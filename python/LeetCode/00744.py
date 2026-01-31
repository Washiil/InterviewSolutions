from typing import List

def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    for c in letters:
        if c > target:
            return c
    return letters[0]