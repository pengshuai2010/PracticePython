import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # will len(nums) >= k? 
        # will k > 0
        # can I modify the input list?
        self.min_heap = list(nums)
        heapq.heapify(self.min_heap)
        self.k = k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]