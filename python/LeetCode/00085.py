from typing import List

def maximalRectangle(self, matrix: List[List[str]]) -> int:
    max_area = 0

    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "0":
                continue

            width = dp[i][j - 1] + 1 if j else 1
            dp[i][j] = width

            for k in range(i, -1, -1):
                width = min(width, dp[k][j])
                max_area = max(max_area, width * (i - k + 1))
    return max_area