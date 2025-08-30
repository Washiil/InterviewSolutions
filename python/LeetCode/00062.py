def uniquePaths(self, m: int, n: int) -> int:
    # Initialize m * n board of zeros
    board = [[0] * n] * m

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                board[i][j] = 1
            else:
                board[i][j] = board[i-1][j] + board[i][j-1]
    
    return board[m - 1][n - 1]
