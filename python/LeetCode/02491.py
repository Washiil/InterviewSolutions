from typing import List

def dividePlayers(self, skill: List[int]) -> int:
    skill.sort()
    n = len(skill)

    right = n - 1
    left = 0

    base_sum = skill[left] + skill[right]

    pairs = []
    while left < right:
        if skill[left] + skill[right] != base_sum:
            return -1
        pairs.append((skill[left], skill[right]))
        left += 1
        right -= 1
    
    chemistry = 0
    for p1, p2 in pairs:
        chemistry += (p1 * p2)
    
    return chemistry