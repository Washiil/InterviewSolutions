# TLE :(

def reverse_and_invert(self, val: int, length: int) -> int:
    result = 0
    for _ in range(length):
        bit = val & 1
        inverted_bit = 1 - bit

        result <<= 1
        result |= inverted_bit
        val >>= 1
    return result

def findKthBit(self, n: int, k: int) -> str:
    s = 0
    current_len = 1

    for i in range(2, n + 1):
        ri_s = self.reverse_and_invert(s, current_len)

        s = (s << (current_len + 1)) | (1 << current_len) | ri_s

        current_len = (current_len * 2) + 1

    full_bin = bin(s)[2:].zfill(current_len)
    return full_bin[k - 1]