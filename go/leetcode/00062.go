package main

func uniquePaths(m int, n int) int {
	board := make([][]int, m)
	for i := range board {
		board[i] = make([]int, n)
	}

	for i := range m {
		for j := range n {
			if i == 0 || j == 0 {
				board[i][j] = 0
			} else {
				board[i][j] = board[i-1][j] + board[i][j-1]
			}
		}
	}
	return board[m-1][n-1]
}
