from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # will there be duplicates in nums?
        # are duplicates in solutions allows?
        # time complexity O(2^n)
        nums.sort()
        solutions = []
        self._dfs(nums, 0, [], solutions)
        return solutions

    def _dfs(self, nums: [int], start: int, partial: [int], solutions: [[int]]):
        solutions.append(list(partial))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            partial.append(nums[i])
            self._dfs(nums, i + 1, partial, solutions)
            partial.pop()
