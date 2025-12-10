def countPermutations(self, complexity: List[int]) -> int:
    """
    You can decrypt the password for the computer i using the password for computer j, where j is any integer less than i with a lower complexity. 
    (i.e. j < i and complexity[j] < complexity[i])
    To decrypt the password for computer i, you must have already unlocked a computer j such that j < i and complexity[j] < complexity[i].

    2 <= complexity.length <= 105
    1 <= complexity[i] <= 109
    """

    start = complexity[0]
    for v in complexity[1:]:
        if v <= start:
            return 0
    
    return math.factorial(len(complexity) - 1) % (10**9 + 7)
