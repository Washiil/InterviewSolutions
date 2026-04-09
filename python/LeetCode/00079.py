def exist(self, board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def search(row: int, col: int, char_idx: int, visited: set) -> bool:
        if row < 0 or row >= m or col < 0 or col >= n or \
           board[row][col] != word[char_idx] or (row, col) in visited:
            return False

        if char_idx == len(word) - 1:
            return True

        visited.add((row, col))

        found = (
            search(row - 1, col, char_idx + 1, visited) or
            search(row + 1, col, char_idx + 1, visited) or
            search(row, col - 1, char_idx + 1, visited) or
            search(row, col + 1, char_idx + 1, visited)
        )


        visited.remove((row, col))

        return found

    for r in range(m):
        for c in range(n):
            if board[r][c] == word[0]:
                if search(r, c, 0, set()):
                    return True

    return False
