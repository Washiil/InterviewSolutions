package main

func searchMatrix(matrix [][]int, target int) bool {
	rows := len(matrix)
	cols := len(matrix[0])

	high := (rows * cols) - 1
	low := 0

	mid := 0
	for low <= high {
		mid = (low + high) / 2

		row := mid / cols
		col := mid % cols

		v := matrix[row][col]
		if v == target {
			return true
		} else if v > target {
			high = mid - 1
		} else if v < target {
			low = mid + 1
		}
	}
	return false
}
