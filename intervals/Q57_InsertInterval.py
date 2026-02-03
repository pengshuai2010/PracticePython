import heapq
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # len(intervals) > 0?
        # newInterval is not None
        # Can I modify input?
        result = []
        heapq.heapify(intervals)
        heapq.heappush(intervals, newInterval)
        while len(intervals) > 0:
            interval = heapq.heappop(intervals)
            if len(result) == 0:
                result.append(interval)
            else:
                last = result[-1]
                if interval[0] <= last[1]:
                    # merge
                    last[1] = max(last[1], interval[1])
                else:
                    result.append(interval)
        return result

