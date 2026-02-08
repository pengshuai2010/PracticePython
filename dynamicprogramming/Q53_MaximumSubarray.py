import math
from typing import List


class Solution:
    def maxSubArray_DynamicProgramming(self, nums: List[int]) -> int:
        # Assuming nums is not empty
        # We keep a subarray only if its sum is greater than 0.
        max_sum = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            # "current" is the max sum of all the subarrays that ends at i
            if current < 0:
                current = 0
            current += nums[i]
            max_sum = max(max_sum, current)
        return max_sum

    def maxSubArray_PrefixSum(self, nums: List[int]) -> int:
        # Use prefixSum
        prefixSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        start = 0
        end = 1
        max_total = - math.inf
        while end <= len(nums):
            total = prefixSum[end] - prefixSum[start]
            max_total = max(max_total, total)
            if total <= 0:
                start = end
            end += 1
        return max_total
