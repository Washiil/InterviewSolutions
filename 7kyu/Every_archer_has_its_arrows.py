def archers_ready(archers):
    if len(archers) > 0:
        return False if min(archers) < 5 else True
    return False