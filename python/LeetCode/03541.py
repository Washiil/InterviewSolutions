from collections import Counter

def maxFreqSum(self, s: str) -> int:
    vowels = 'aeiou'
    counts = Counter(s)
    v_count = 0
    c_count = 0

    for key, val in counts.items():
        if key in vowels:
            v_count = max(v_count, val)
        else:
            c_count = max(c_count, val)

    return v_count + c_count
