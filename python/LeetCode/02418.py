from typing import List

def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    return [x for _, x in sorted(zip(heights, names), key=lambda pair: pair[0], reverse=True)]