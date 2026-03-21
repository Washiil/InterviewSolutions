package main

func reverseSubmatrix(grid [][]int, x int, y int, k int) [][]int {
	for i := range k / 2 {
		row1 := x + i
		row2 := x + k - 1 - i

		for c := range k {
			col := y + c
			grid[row1][col], grid[row2][col] = grid[row2][col], grid[row1][col]
		}
	}

	return grid
}
