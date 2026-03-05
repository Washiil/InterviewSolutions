def minOperations(self, s: str) -> int:
    # consider the following two cases
    # case 1 s starts with 0
    # case 2 s starts with 1

    case1 = 0
    case2 = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == '1':
                case1 += 1
            else:
                case2 += 1
        else:
            if s[i] == '1':
                case2 += 1
            else:
                case1 += 1

    return min(case1, case2)
