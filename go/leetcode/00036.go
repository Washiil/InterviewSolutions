package main

func isValidSudoku(board [][]byte) bool {
	n := 9

	var rows [9][9]bool
	var cols [9][9]bool
	var boxes [9][9]bool

	for r := range n {
		for c := range n {
			char := board[r][c]

			if char == '.' {
				continue
			}

			num := char - '1'
			boxIndex := (r/3)*3 + c/3

			if rows[r][num] || cols[c][num] || boxes[boxIndex][num] {
				return false
			}

			rows[r][num] = true
			cols[c][num] = true
			boxes[boxIndex][num] = true
		}
	}

	return true
}
