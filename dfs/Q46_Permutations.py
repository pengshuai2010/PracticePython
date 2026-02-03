class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Will there be duplicates in the nums?
        # Time complexity O(n*n!) There are n! solutions, and it takes O(n) to copy one solution.
        solutions = []
        self._dfs(nums, [False for _ in nums], [], solutions)
        return solutions

    def _dfs(self, nums: [int], visited: [bool], partial: [int], solutions: [[int]]) -> None:
        if len(partial) == len(nums):
            solutions.append(list(partial))
            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                partial.append(nums[i])
                self._dfs(nums, visited, partial, solutions)
                visited[i] = False
                partial.pop()