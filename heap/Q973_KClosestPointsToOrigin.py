import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # can I modify the input?
        # k <= len(points)?
        # k > 0?
        return heapq.nsmallest(k, points, lambda point: point[0] * point[0] + point[1] * point[1])

    # Time complexity: O(n) for constructing list of items, O(n) for heapify.
    # O(k * log(n)) for pulling out k smallest items out of the min heap
    # Overall O(n + k * log(n))
    def kClosest_MinHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
        # can I modify the input?
        # k <= len(points)?
        # k > 0?
        # How do you break a tie? IMPORT question to ask in problems regarding sorting.
        items = [(point[0] * point[0] + point[1] * point[1], point) for point in points]
        heapq.heapify(items)
        answer = []
        while len(answer) < k:
            point = heapq.heappop(items)[1]
            answer.append(point)
        return answer

    # Time complexity: O(n) for constructing list of items, O(n) for heapify.
    # O(n * log(k)) for going over n items.
    # Overall O(n + n * log(k))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # can I modify the input?
        # k <= len(points)?
        # k > 0?
        # How do you break a tie? IMPORT question to ask in problems regarding sorting.
        items = [(point[0] * point[0] + point[1] * point[1], point) for point in points]
        max_heap = []
        for item in items:
            heapq.heappush_max(max_heap, item)
            while len(max_heap) > k:
                heapq.heappop_max(max_heap)
        return [point for distance_squared, point in max_heap]


    # Quick partition. Time complexity O(n)
    
