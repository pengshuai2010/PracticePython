import heapq
from typing import List


class Solution:

    # Comparing min heap and max heap approach.
    # When k is much smaller than n, it's better to min heap approach, because it takes less memory.
    # min heap approach also works when you have a stream of data.

    def findKthLargest_maxHeap(self, nums: List[int], k: int) -> int:
        # Can I modify the input list?
        # k <= len(nums)?
        # k > 0?
        # Time complexity: O(n) to heapify, O(k*log(n)) to get kth largest element, overall
        # time complexity is O(n + k*log(n))
        # Memory complexity O(n)
        heapq.heapify_max(nums)
        for i in range(k - 1):
            heapq.heappop_max(nums)
        return heapq.heappop_max(nums)

    def findKthLargest_minHeap(self, nums: List[int], k: int) -> int:
        # Can I modify the input list?
        # k <= len(nums)?
        # k > 0?
        # Time complexity: O(n*log(k))
        # Memory complexity: O(k)
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]