def sortVowels(self, s: str) -> str:
    vowels = sorted([i for i in s if i.lower() in 'aeiou'], reverse=True)
    return ''.join([vowels.pop() if i.lower() in 'aeiou' else i for i in s])
