def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
    a_set = set()
    b_set = set()
    n = len(A)
    output = [0] * n

    for i in range(n):
        a_set.add(A[i])
        b_set.add(B[i])
        output[i] = i - len(a_set - b_set) + 1

    return output
