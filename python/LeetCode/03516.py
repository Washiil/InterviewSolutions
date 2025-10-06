def findClosest(self, x: int, y: int, z: int) -> int:
    x_dist = abs(z-x)
    y_dist = abs(z-y)
    if x_dist == y_dist:
        return 0
    elif y_dist > x_dist:
        return 1
    else:
        return 2
