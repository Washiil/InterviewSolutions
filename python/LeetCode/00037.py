from typing import List

def generateValidMoves(row: int, col: int, board: List[List[str]]):
    n = len(board)
    seen = []
    for i in range(n):
        seen.append(board[row][i])

    for i in range(n):
        seen.append(board[i][col])

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            seen.append(board[i][j])

    return [str(x) for x in range(1, n + 1) if str(x) not in seen]

def solveSudoku(board: List[List[str]]) -> None:
    solve(board)

def solve(board: List[List[str]]) -> bool:
    n = len(board)
    
    # use Most constrained variable approach
    min_moves = float('inf')
    best_cell = None
    
    for r in range(n):
        for c in range(n):
            if board[r][c] == ".":
                moves = generateValidMoves(r, c, board)
                num_moves = len(moves)
                
                if num_moves == 0:
                    return False
                
                if num_moves < min_moves:
                    min_moves = num_moves
                    best_cell = (r, c, moves)
    
    # Base Case
    if best_cell is None:
        return True
    
    row, col, moves = best_cell
    
    for move in moves:
        board[row][col] = move
        if solve(board):
            return True
        board[row][col] = "."
        
    return False