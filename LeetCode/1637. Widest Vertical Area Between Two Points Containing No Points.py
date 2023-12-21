def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
    x_coords = sorted([point[0] for point in points])

    big_diff = 0

    for i in range(len(x_coords) - 1):
        big_diff = max(big_diff, x_coords[i + 1] - x_coords[i])

    return big_diff
