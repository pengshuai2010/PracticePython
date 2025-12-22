from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # will nums be empty? Could it be that there were no rotation?
        # rotating n time is equivalent to no rotation!
        start = 0
        end = len(nums) - 1
        # All numbers are unique. So nums[start] == nums[end] means there is only one element.
        # And nums[start] < nums[end] means there is no rotation.
        if nums[start] <= nums[end]: # no rotation
            return nums[start]
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[start] < nums[mid]:
                start = mid
            else: # all numbers are unique, so no equal case
                end = mid
        return min(nums[start], nums[end])

    def findMin_compare_with_end(self, nums: List[int]) -> int:
        # will nums be empty? Could it be that there were no rotation?
        # rotating n time is equivalent to no rotation!
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            # all numbers are unique, so no equal case
            # when nums[mid] < nums[end], either there was rotation and the first element of original array is
            # at the left, or there was no rotation and nums[start] is the first element. In either case, we
            # move the end to mid.
            else:
                end = mid
        return min(nums[start], nums[end])
