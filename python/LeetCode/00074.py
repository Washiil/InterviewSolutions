from typing import List

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])

    high = (rows * cols) - 1
    low = 0
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        row = mid // cols
        col = mid % cols

        guess = matrix[row][col]

        if guess == target:
            return True
        elif guess > target:
            high = mid - 1
        elif guess < target:
            low = mid + 1

    return False