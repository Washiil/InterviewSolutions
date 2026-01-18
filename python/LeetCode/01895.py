from typing import List

def largestMagicSquare(self, grid: List[List[int]]) -> int:
    largest_area = 0

    m = len(grid)
    n = len(grid[0])

    def check_box(row: int, col: int, size: int) -> bool:
        area = sum(grid[row][col:col + size])
        valid = True

        # Check rows
        for offset in range(size):
            if sum(grid[row + offset][col:col + size]) != area:
                valid = False
                break

        for offset in range(size):
            tmp = 0
            for idx in range(size):
                tmp += grid[row + idx][col + offset]
            if tmp != area:
                valid = False
                break

        diag1 = 0
        diag2 = 0
        for offset in range(size):
            diag1 += grid[row + offset][col + offset]
            diag2 += grid[row + offset][col + size - 1 - offset]

        if diag1 != area or diag2 != area:
            valid = False
        return valid

    for size in range(min(m, n)):
        for row in range(m - size):
            for col in range(n - size):
                if check_box(row, col, size + 1):
                    largest_area = size + 1

    return largest_area