from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # what if nums is empty?
        # invariant: all the elements before slow pointer are non-zero elements in their final position
        # elements between fast pointer and slow pointer are zeros
        # Always move fast pointer. Move slow pointer only if it points to a non-zero.
        q = 0
        for p in range(len(nums)):
            if nums[p] != 0 and nums[q] == 0:
                tmp = nums[p]
                nums[p] = nums[q]
                nums[q] = tmp
            if nums[q] != 0:
                q += 1
# [0]
# [1]
# [0, 1]
# [1, 0]