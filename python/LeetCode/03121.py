def numberOfSpecialChars(self, word: str) -> int:
    lower_seen = set()
    upper_seen = set()
    invalid = set()
    valid = set()
    for c in word:
        if c in invalid:
            continue
        cup = c.upper()
        clow = c.lower()

        if c.isupper():
            if clow not in lower_seen:
                invalid.add(c)
                invalid.add(clow)
                continue
            upper_seen.add(c)
            valid.add(c)
        else:
            if cup in upper_seen:
                invalid.add(c)
                invalid.add(cup)
                continue
            lower_seen.add(c)

    return len(valid - invalid)
