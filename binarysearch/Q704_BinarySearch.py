from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Is target guaranteed in the nums? What to return if not found?
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2 # must be integer divide in index arithmetics
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1