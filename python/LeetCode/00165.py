def compareVersion(self, version1: str, version2: str) -> int:
    v1 = [int(x) for x in version1.split('.')]
    v2 = [int(x) for x in version2.split('.')]

    n1 = len(v1)
    n2 = len(v2)

    n = max(n1, n2)

    for i in range(n):
        if i >= n1:
            if v2[i] > 0:
                return -1
            continue

        if i >= n2:
            if v1[i] > 0:
                return 1
            continue
        
        # Both in rnage
        if v1[i] > v2[i]:
            return 1
        elif v1[i] < v2[i]:
            return -1
        
    return 0
