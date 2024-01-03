def numberOfBeams(self, bank: list[str]) -> int:
    lasers = 0
    # Count of security devices in each row
    sec_counts = [row.count('1') for row in bank if row.count('1') > 0]

    if len(sec_counts) == 0:
        return lasers
    
    for i in range(len(sec_counts) - 1):
        lasers += sec_counts[i] * sec_counts[i + 1]
    
    return lasers