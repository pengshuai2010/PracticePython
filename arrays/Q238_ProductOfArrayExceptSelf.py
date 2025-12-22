from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # clarify: will there be overflow? nums is empty or size == 1?
        # prefix_product[i] = nums[0] * ... * nums[i - 1]
        # suffix_product[i] = nums[i + 1] * ... * nums[n - 1]
        n = len(nums)
        prefix_product = [0] * n
        prefix_product[0] = 1
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        suffix_product = [0] * n
        suffix_product[n - 1] = 1
        for index in range(n - 2, -1, -1):
            suffix_product[index] = suffix_product[index + 1] * nums[index + 1]
        result = [0] * n
        for i in range(n):
            result[i] = prefix_product[i] * suffix_product[i]
        return result

    def productExceptSelf_constantExtraSpace(self, nums: List[int]) -> List[int]:
        # Store the suffix product in the output list, and calculate prefix product on the fly
        n = len(nums)
        result = [0] * n
        result[n - 1] = 1
        for index in range(n - 2, -1, -1):
            result[index] = result[index + 1] * nums[index + 1]
        prefix_product = 1
        for i in range(n):
            result[i] = prefix_product * result[i]
            prefix_product *= nums[i]
        return result