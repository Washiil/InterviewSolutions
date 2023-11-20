from collections import defaultdict


def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
    pref = [0]

    for time in travel:
        pref.append(pref[-1]+time)

    lind = defaultdict(int)
    for i, units in enumerate(garbage):
        for u in units:
            lind[u] = i

    total = sum(map(len, garbage))
    x = [pref[lind[t]] for t in lind.keys()]
    return total + sum(x)
