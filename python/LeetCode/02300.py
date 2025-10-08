def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    n = len(spells)
    m = len(potions)

    output = [0 for _ in range(n)]

    @lru_cache
    def compute_combos(idx: int) -> int:
        count = 0
        spell = spells[idx]
        for j in range(m):
            v = potions[j] * spell
            if v >= success:
                count += 1
        return count

    for i in range(n):
        output[i] = compute_combos(i)
    
    return output