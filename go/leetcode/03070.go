package main

func countSubmatrices(grid [][]int, k int) int {
	m := len(grid)
	n := len(grid[0])
	output := 0

	for row := range m {
		for col := range n {
			if row > 0 {
				grid[row][col] += grid[row-1][col]
			}
			if col > 0 {
				grid[row][col] += grid[row][col-1]
			}

			if row > 0 && col > 0 {
				grid[row][col] -= grid[row-1][col-1]
			}

			if grid[row][col] <= k {
				output += 1
			}
		}
	}

	return output
}
