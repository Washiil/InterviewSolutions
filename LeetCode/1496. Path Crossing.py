from collections import defaultdict 

def isPathCrossing(self, path: str) -> bool:
    visited = defaultdict()
    visited[(0, 0)] = 1

    coords = [0, 0]
    for c in path:
        if c == 'N':
            coords[1] += 1
        elif c == 'S':
            coords[1] -= 1
        elif c == 'E':
            coords[0] += 1
        elif c == 'W':
            coords[0] -= 1
        if (coords[0], coords[1]) in visited:
            return True
        else:
            visited[(coords[0], coords[1])] = 1
    
    return False