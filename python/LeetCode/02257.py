def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    '''
    Assumptions:
        A guard can see every cell in the four cardinal directions (north, east, south, or west)
            - Unless obstructed by a wall or another guard
        A cell is guarded if there is at least one guard that can see it
        Return the number of unoccupied cells that are not guarded.
    
    Plan:
        Construct m x n boolean matrix
        0 Represent a square that is not visible
        iterate over guards and check all directions, set all the values they can see to 0
        return the sum of all values
    '''

    grid = [[0 for _ in range(n)] for _ in range(m)]

    for w in walls:
        row, col = w[0], w[1]
        grid[row][col] = -1

    for g in guards:
        row, col = g[0], g[1]
        grid[row][col] = 1

    # Debug Print
    for r in grid:
        for v in r:
            print(f'{v:>3}', end='')
        print('')
        
    total = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] != 0:
                continue
            # Left
            seen = False

            col_idx = col-1
            while col_idx >= 0:
                if grid[row][col_idx] == -1:
                    break
                elif grid[row][col_idx] == 1:
                    seen = True
                    break
                col_idx -= 1
            
            if seen:
                continue

            # Right
            col_idx = col+1
            while col_idx < n:
                if grid[row][col_idx] == -1:
                    break
                elif grid[row][col_idx] == 1:
                    seen = True
                    break
                col_idx += 1

            if seen:
                continue
            # Up
            row_idx = row-1
            while row_idx >= 0:
                if grid[row_idx][col] == -1:
                    break
                elif grid[row_idx][col] == 1:
                    seen = True
                    break
                row_idx -= 1

            if seen:
                continue

            # DOwn
            row_idx = row+1
            while row_idx < m:
                if grid[row_idx][col] == -1:
                    break
                elif grid[row_idx][col] == 1:
                    seen = True
                    break
                row_idx += 1

            if seen:
                continue

            total += 1

    return total
