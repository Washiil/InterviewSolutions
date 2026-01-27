from typing import List
from collections import defaultdict
import heapq

def minCost(self, n: int, edges: List[List[int]]) -> int:
    traversal = defaultdict(list)
    for src, dest, cost in edges:
        traversal[src].append([dest, cost])
        traversal[dest].append([src, 2 * cost])

    dist = [float('inf')] * n
    dist[0] = 0
    # Keep track of the distance in node for djikstras (distance, node)
    heap = [(0, 0)]

    while heap:
        curr_dist, node = heapq.heappop(heap)

        if node == n - 1:
            return curr_dist

        for y, cost in traversal[node]:
            updated_distance = curr_dist + cost
            if updated_distance < dist[y]:
                dist[y] = updated_distance
                heapq.heappush(heap, (updated_distance, y))

    return -1
