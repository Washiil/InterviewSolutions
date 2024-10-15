def minimumSteps(self, s: str) -> int:
    total_swaps = 0
    black_ball_count = 0

    # Iterate through each ball in the string
    for char in s:
        if char == "0":
            total_swaps += black_ball_count
        else:
            black_ball_count += 1

    return total_swaps