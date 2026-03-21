package main

import (
	"math"
	"slices"
	"sync"
)

func checkSubmatrix(grid [][]int, row int, col int, k int, ans [][]int) {
	vals := make([]int, 0, k*k)

	for dr := 0; dr < k; dr++ {
		vals = append(vals, grid[row+dr][col:col+k]...)
	}

	slices.Sort(vals)

	minDiff := math.MaxInt32
	foundUnique := false

	for i := 0; i < len(vals)-1; i++ {
		if vals[i] == vals[i+1] {
			continue
		}

		diff := vals[i+1] - vals[i]
		if diff < minDiff {
			minDiff = diff
			foundUnique = true
		}
	}

	if foundUnique {
		ans[row][col] = minDiff
	}
}

func minAbsDiff(grid [][]int, k int) [][]int {
	// Nice parallel implementation im proud of
	m := len(grid)
	n := len(grid[0])

	ans := make([][]int, m-k+1)

	// Initialize each inner slice
	for i := range ans {
		ans[i] = make([]int, n-k+1)
	}

	var wg sync.WaitGroup

	for row := range m {
		if row+k > m {
			break
		}
		wg.Add(1)
		go func(r int) {
			defer wg.Done()
			for c := range n {
				if c+k > n {
					break
				}
				checkSubmatrix(grid, r, c, k, ans)
			}
		}(row)
	}

	wg.Wait()

	return ans
}
