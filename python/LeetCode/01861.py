from typing import List

def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
    n = len(boxGrid)
    m = len(boxGrid[0])

    for row in range(n - 1, -1, -1):
        stone_index = m - 1
        for col in range(m - 1, -1, -1):
            if boxGrid[row][col] == '.':
                continue
            elif boxGrid[row][col] == '*':
                # Update index
                stone_index = col - 1
            elif boxGrid[row][col] == '#':
                # Bring stone down
                boxGrid[row][col] = '.'
                boxGrid[row][stone_index] = '#'
                stone_index -= 1

    rotated = [list(row) for row in zip(*boxGrid[::-1])]

    return rotated
