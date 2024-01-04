def reverseWords(self, s: str) -> str:
    sanitized = ''
    recent = ' '
    for c in s.strip():
        if recent == ' ' and c == ' ':
            continue
        sanitized += c
        recent = c

    return ' '.join(reversed(sanitized.split(' ')))
