def maximumEnergy(self, energy: List[int], k: int) -> int:
    max_energy = sum([abs(x) for x in energy]) * -1
    n = len(energy)

    for start in range(n):
        idx = start
        current_energy = 0
        while idx < n:
            current_energy += energy[idx]
            idx += k
        
        max_energy = max(max_energy, current_energy)
    
    return max_energy