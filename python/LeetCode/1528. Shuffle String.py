def restoreString(self, s: str, indices: list[int]) -> str:
    output = [0] * len(s)
    for i, v in enumerate(indices):
        output[v] = s[i]

    return ''.join(output)