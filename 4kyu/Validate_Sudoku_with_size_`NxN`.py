from collections import defaultdict
from math import sqrt

class Sudoku(object):
    def __init__(self, data):
        self.board = data
        self.n = len(data)
        self.magic_num = sqrt(self.n)
        
    def is_valid(self):
        rows, cols = defaultdict(set), defaultdict(set)
        squares = defaultdict(set)

        for r in range(self.n):
            for c in range(self.n):
                value = self.board[r][c]
                if type(value) != int or 1 < value > self.n:
                    return False
                square_index = (r // self.magic_num, c // self.magic_num)
                if (value == 0 or
                    value in rows[r] or
                    value in cols[c] or
                    value in squares[square_index]
                   ):
                    return False
                rows[r].add(value)
                cols[c].add(value)
                squares[square_index].add(value)
        return True