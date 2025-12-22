from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # will piles be empty? guarantee h > 0
        # will there be empty pile?
        start = max(sum(piles) // h, 1)  # start is at least 1
        end = max(piles)  # Koko can only eat one pile in one hour, there is no need to go higher.
        while start + 1 < end:
            mid = (start + end) // 2
            if self._can_finish(piles, mid, h):
                end = mid
            else:
                start = mid
        if self._can_finish(piles, start, h):
            return start
        return end

    def _can_finish(self, piles: List[int], k: int, h: int) -> bool:
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)  # eating a pile of 1 banana with k = 2 takes 1 hour
        return time <= h

# test cases
# piles = [1], h = 2
# time complexity: O(n * log(m)), where n is the number of piles, and m is the max number of bananas in a single pile from piles.