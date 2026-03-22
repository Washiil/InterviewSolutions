package main

import "sync"

func findRotation(mat [][]int, target [][]int) bool {
	rotations := []bool{true, true, true, true}
	n := len(mat)

	var wg sync.WaitGroup

	for i := 0; i < n; i++ {
		wg.Add(1)
		go func(r int) {
			defer wg.Done()
			for j := 0; j < n; j++ {
				if mat[r][j] != target[r][j] {
					rotations[0] = false
				}

				if mat[n-1-j][r] != target[r][j] {
					rotations[1] = false
				}

				if mat[n-1-r][n-1-j] != target[r][j] {
					rotations[2] = false
				}

				if mat[j][n-1-r] != target[r][j] {
					rotations[3] = false
				}
			}
		}(i)
	}

	wg.Wait()

	for _, v := range rotations {
		if v {
			return true
		}
	}

	return false
}
