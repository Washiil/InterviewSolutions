import math
from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # -2 turn left 90
        # -1 turn right 90
        # Anything else move forwards that many squares (one at a time / optimize for obstacles)
        obstacles = set(tuple(coord) for coord in obstacles) # for O(1) lookup
        max_distance = 0
        furthest_point = (0, 0)
        direction = 0 # North 0, East 1, South 2, West, 3
        x, y = 0, 0

        def calculate_distance(x1, y1, x2, y2):
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        for command in commands:
            # Handle right turn
            if command == -1:
                if direction == 3:
                    direction = 0
                else:
                    direction += 1
            # Handle right turn
            elif command == -2:
                if direction == 0:
                    direction = 3
                else:
                    direction -= 1
            # Perform move operation
            else:
                match direction:
                    case 0:
                        for _ in range(command):
                            y += 1
                            if (x, y) in obstacles:
                                y -= 1
                                break
                    case 1:
                        for _ in range(command):
                            x += 1
                            if (x, y) in obstacles:
                                x -= 1
                                break
                    case 2:
                        for _ in range(command):
                            y -= 1
                            if (x, y) in obstacles:
                                y += 1
                                break
                    case 3:
                        for _ in range(command):
                            x -= 1
                            if (x, y) in obstacles:
                                x += 1
                                break
                    case _:
                        print(f'Invalid direction: {direction}')
                        exit(0)
                
                new_dist = calculate_distance(x, y, 0, 0)

                if max_distance < new_dist:
                    max_distance = new_dist
                    furthest_point = (x, y)

        
        return (furthest_point[0] ** 2) + (furthest_point[1] ** 2)
