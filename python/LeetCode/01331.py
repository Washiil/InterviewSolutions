from typing import List

def arrayRankTransform(self, arr: List[int]) -> List[int]:
    ranks = {element: rank + 1 for rank, element in enumerate(sorted(set(arr)))}
    return [ranks[x] for x in arr]