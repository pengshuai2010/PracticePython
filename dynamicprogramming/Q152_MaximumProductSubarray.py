from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # will there be zero? negative number?
        # assuming nums is not empty
        max_sofar = nums[0]
        min_sofar = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            current = nums[i]
            updated_max_sofar = max(current, max_sofar * current, min_sofar * current)
            updated_min_sofar = min(current, max_sofar * current, min_sofar * current)
            max_sofar, min_sofar = updated_max_sofar, updated_min_sofar
            result = max(result, max_sofar)
        return result