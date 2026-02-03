from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # will nums be empty?

        solutions = []
        self._helper(nums, 0, [], solutions)
        return solutions

    def _helper(self, nums, start, partial, solutions):
        solutions.append(list(partial))
        for i in range(start, len(nums)):
            partial.append(nums[i])
            self._helper(nums, i + 1, partial, solutions)
            partial.pop()
