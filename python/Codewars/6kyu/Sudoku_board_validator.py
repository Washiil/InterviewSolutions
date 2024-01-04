from collections import defaultdict

def validate_sudoku(board):
    rows, cols = defaultdict(set), defaultdict(set)
    squares = defaultdict(set)
    
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if (value == 0 or
                value in rows[r] or
                value in cols[c] or
                value in squares[(r // 3, c // 3)]
               ):
                return False
            rows[r].add(value)
            cols[c].add(value)
            squares[(r // 3, c // 3)].add(value)
    return True