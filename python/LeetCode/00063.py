from typing import List

def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1:
        return 0

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    board = [[0] * n for _ in range(m)]
    board[0][0] = 1

    for i in range(m):
        for j in range(n):
            # Obstacle check leave 0
            if obstacleGrid[i][j] == 1:
                continue
            if i == 0 and j == 0:
                continue

            if i == 0:
                board[i][j] = board[i][j-1]
            elif j == 0:
                board[i][j] = board[i-1][j]
            else:
                board[i][j] = board[i-1][j] + board[i][j-1]

    return board[m-1][n-1]
