def destCity(self, paths: list[list[str]]) -> str:
    directions = {}
    for path in paths:
        directions[path[0]] = path[1]

    current_path = paths[0][0]
    while current_path in directions.keys():
        current_path = directions[current_path]

    return current_path
