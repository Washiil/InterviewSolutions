def get_participants(h):
    if h == 0:
        return 0
    k = 1
    i = 0
    while i < h:
        i += k
        k += 1
    return k
