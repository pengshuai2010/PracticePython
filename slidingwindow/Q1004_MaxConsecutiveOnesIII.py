from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # assuming k > 0
        s = 0
        e = 0
        zeros = 0
        longest = 0
        while e < len(nums):
            if nums[e] == 0:
                zeros += 1
            # the invariant is zeros <= k
            # restore invariant
            while zeros > k:
                if nums[s] == 0:
                    zeros -= 1
                s += 1
            # invariant is restored
            longest = max(longest, e - s + 1)
            # in the loop, we need an increment state to break the invariant, otherwise the loop could stuck
            e += 1
        return longest