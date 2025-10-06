from functools import lru_cache

@lru_cache
def gcd(self, x: int, y: int) -> int:
    i = max(x, y)
    while i > 0:
        if x % i == 0 and y % i == 0:
            return i
        else:
            i -= 1
    
    # Unreachable
    return 1

@lru_cache
def lcm(self, x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    return abs(x * y) // self.gcd(x, y)

def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
    stack = []

    for num in nums:
        current_num = num

        while stack and self.gcd(stack[-1], current_num) > 1:
            last_element = stack.pop()
            current_num = self.lcm(last_element, current_num)

        stack.append(current_num)

    return stack
