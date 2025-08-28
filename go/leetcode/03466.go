package main

import (
	"sort"
)

func sortMatrix(grid [][]int) [][]int {
	n := len(grid)

	// Top right
	for col := 1; col < n; col++ {
		tmp := make([]int, n-col)
		idx := 0
		for row := 0; row < n-col; row++ {
			tmp[idx] = grid[row][col+row]
			idx++
		}
		idx = 0
		sort.Ints(tmp)

		for row := 0; row < n-col; row++ {
			grid[row][col+row] = tmp[idx]
			idx++
		}
	}

	// Bottom left
	for row := 0; row < n; row++ {
		tmp := make([]int, n-row)
		idx := 0
		for col := 0; col < n-row; col++ {
			tmp[idx] = grid[row+col][col]
			idx++
		}
		idx = 0
		sort.Sort(sort.Reverse(sort.IntSlice(tmp)))
		for col := 0; col < n-row; col++ {
			grid[row+col][col] = tmp[idx]
			idx++
		}
	}

	return grid
}
