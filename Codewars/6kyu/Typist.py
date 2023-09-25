def typist(s):
    presses = 0
    caps = False
    for c in s:
        if c.isupper():
            if caps:
                presses += 1
            else:
                caps = True
                presses += 2
        else:
            if caps:
                caps = False
                presses += 2
            else:
                presses += 1
    return presses