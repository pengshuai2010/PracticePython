import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # what if no stone left? e.g. [1, 1]
        max_heap = list(stones)
        heapq.heapify_max(max_heap)
        while len(max_heap) > 1:
            y = heapq.heappop_max(max_heap)
            x = heapq.heappop_max(max_heap)
            remain = y - x
            if remain > 0:
                heapq.heappush_max(max_heap, remain)
        if len(max_heap) > 0:
            return max_heap[0]
        return 0