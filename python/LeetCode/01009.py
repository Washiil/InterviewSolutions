def bitwiseComplement(self, n: int) -> int:
    b = bin(n)[2:]
    z = ['1' if x == '0' else '0' for x in b]
    return int(''.join(z), 2)
