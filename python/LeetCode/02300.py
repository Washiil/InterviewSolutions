def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    n = len(spells)
    m = len(potions)

    output = [0 for _ in range(n)]

    for i in range(n):
        spell = spells[i]
        for j in range(m):
            v = potions[j] * spell
            if v >= success:
                output[i] += 1
    
    return output