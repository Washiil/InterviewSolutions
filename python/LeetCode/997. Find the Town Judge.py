def findJudge(self, n: int, trust: List[List[int]]) -> int:
    people = [0] * (n + 1)

    for a,b in trust:
        people[a] -= 1
        people[b] += 1
    
    for i in range(1, n + 1):
        if people[i] == n -1:
            return i
    
    return -1