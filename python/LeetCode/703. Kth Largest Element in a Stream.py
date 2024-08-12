import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        # Initialize the heap with the first k elements from nums
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        # If the heap has fewer than k elements, just add the new value
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # If the heap is full and the new value is larger than the smallest element
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
        
        # The root of the heap is the k-th largest element
        return self.min_heap[0]
