from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = -1
        n = len(nums) - 1
        for num in nums:
            index = abs(num)
            if nums[index] < 0:
                duplicate = index
                break
            else:
                nums[index] = - nums[index]
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return duplicate