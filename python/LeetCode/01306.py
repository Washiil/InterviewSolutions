def canReach(self, arr: list[int], start: int) -> bool:
    n = len(arr)
    visited = [False] * n

    def explore(idx: int):
        if idx < 0 or idx >= n or visited[idx]:
            return False

        v = arr[idx]
        if v == 0:
            return True

        visited[idx] = True

        return explore(idx - v) or explore(idx + v)

    return explore(start)
