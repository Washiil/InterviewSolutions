from typing import List

def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    adjacency_map = {i: [] for i in range(n)}

    for origin, destination in edges:
        adjacency_map[destination].append(origin)
    
    # Memoization Table for each value
    memoization = {}

    def find_ancestors(child: int):
        if child in memoization:
            return memoization[child]
        
        ancestors = set(adjacency_map[child])
        for ancestor in adjacency_map[child]:
            ancestors.update(find_ancestors(ancestor))
        
        memoization[child] = sorted(ancestors)
        return memoization[child]
    
    output = []
    for key in adjacency_map:
        if key not in memoization:
            memoization[key] = sorted(find_ancestors(key))
        
        output.append(memoization[key])
    
    return output
