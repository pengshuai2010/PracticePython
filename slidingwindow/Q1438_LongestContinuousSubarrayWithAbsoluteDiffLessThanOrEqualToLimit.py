import heapq
from collections import defaultdict
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # limit >= 0
        min_heap = []
        max_heap = []
        mapping = defaultdict(set)
        left = 0
        right = 0
        longest = 0

        while right < len(nums):
            heapq.heappush(min_heap, nums[right])
            heapq.heappush_max(max_heap, nums[right])
            mapping[nums[right]].add(right)
            while max_heap[0] - min_heap[0] > limit:
                mapping[nums[left]].remove(left) # there will be stale values in the heaps, but we will remove them when we access the heap tops.
                while len(mapping[min_heap[0]]) == 0: # there could be consecutive elements that have 0 count now.
                    heapq.heappop(min_heap)
                while len(mapping[max_heap[0]]) == 0:
                    heapq.heappop_max(max_heap)
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest

if __name__ == '__main__':
    Solution().longestSubarray([8,2,4,7], 4)