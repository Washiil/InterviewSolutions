package main

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if obstacleGrid[0][0] == 1 {
		return 0
	}

	m := len(obstacleGrid)
	n := len(obstacleGrid[0])

	board := make([][]int, m)
	for i := range m {
		board[i] = make([]int, n)
	}
	board[0][0] = 1

	for i := range m {
		for j := range n {
			if i == 0 && j == 0 {
				continue
			}
			if obstacleGrid[i][j] == 1 {
				continue
			}

			if i == 0 {
				board[i][j] = board[i][j-1]
			} else if j == 0 {
				board[i][j] = board[i-1][j]
			} else {
				board[i][j] = board[i-1][j] + board[i][j-1]
			}
		}
	}

	return board[m-1][n-1]
}
