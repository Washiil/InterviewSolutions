def heightChecker(self, heights: list[int]) -> int:
    x = sorted(heights)
    return len([i for i in range(len(heights)) if x[i] != heights[i]])