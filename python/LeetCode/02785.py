def sortVowels(self, s: str) -> str:
    vowels = [ord(c) for c in 'aeiouAEIOU']
    parsed = [ord(c) for c in s]

    indexes = [i for i in range(len(parsed)) if parsed[i] in vowels]
    new_vowels = sorted([parsed[c] for c in indexes])

    for i, v in zip(indexes, new_vowels):
        parsed[i] = v
    
    return ''.join([chr(c) for c in parsed])
