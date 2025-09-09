def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    # Counts in each subgroup
    state = [0] * n
    state[0] = 1
    
    # State from one because day1 A is told
    for i in range(1, n):
        state = [0] + state[:-1]
        state[0] = sum(state[delay:forget])
    
    return sum(state[:forget]) % (10 ** 9 + 7)
