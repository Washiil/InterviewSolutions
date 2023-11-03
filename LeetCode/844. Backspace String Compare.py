def backspaceCompare(self, s: str, t: str) -> bool:
    s1 = []
    t1 = []
    for c in s:
        if c == '#':
            if len(s1) > 0:
                s1.pop()
        else:
            s1.append(c)

    for c in t:
        if c == '#':
            if len(t1) > 0:
                t1.pop()
        else:
            t1.append(c)

    return s1 == t1
